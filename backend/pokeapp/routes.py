from http import HTTPStatus
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pokeapp.database.connection import get_db
from pokeapp.repository.respository import register_user, autenticate_user
from pokeapp.schemas.schemas import UserPublic, UserSchema, Token
from fastapi.security import OAuth2PasswordRequestForm
from pokeapp.security import get_current_user, create_access_token
from pokeapp.redis_client import redis_client
import requests
import json

router = APIRouter(prefix="/api")

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon"
POKEAPI_SPECIES_URL = "https://pokeapi.co/api/v2/pokemon-species"


@router.get("/")
async def get_all_pokemons(
    current_user=Depends(get_current_user), limit: int = 6, offset: int = 0
):
    try:
        cache_key = f"pokemons_{offset}_{limit}"

        cached_pokemons = redis_client.get(cache_key)

        if cached_pokemons:
            return json.loads(cached_pokemons)

        response = requests.get(f"{POKEAPI_URL}?limit={limit}&offset={offset}")
        response.raise_for_status()
        pokemons = response.json()

        pokemon_details_list = []

        for pokemon in pokemons["results"]:
            pokemon_info_response = requests.get(pokemon["url"])
            pokemon_info_response.raise_for_status()
            pokemon_details = pokemon_info_response.json()

            pokemon_image_url = pokemon_details["sprites"]["front_default"]

            species_info_response = requests.get(
                f"{POKEAPI_SPECIES_URL}/{pokemon_details['id']}"
            )
            species_info_response.raise_for_status()
            species_details = species_info_response.json()

            color = species_details["color"]["name"]

            pokemon_details_list.append(
                {"name": pokemon["name"], "image": pokemon_image_url, "color": color}
            )

        result = {
            "count": pokemons["count"],
            "next": pokemons["next"],
            "previous": pokemons["previous"],
            "results": pokemon_details_list,
        }

        redis_client.setex(cache_key, 3600, json.dumps(result))

        return result

    except requests.exceptions.RequestException as error:
        raise HTTPException(status_code=500, detail=str(error))


@router.post("/register", status_code=HTTPStatus.CREATED, response_model=UserPublic)
async def create_user(
    user: UserSchema,
    session: Session = Depends(get_db),
):
    new_user = register_user(session, user.username, user.password)
    return new_user


@router.post("/login", response_model=Token)
async def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_db)
):
    user = autenticate_user(
        session, username=form_data.username, password=form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail="Usuário ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data_payload={"sub": user.username})

    redis_client.setex(f"user_session_{user.username}", 20, access_token)

    return {"access_token": access_token, "token_type": "Bearer"}
