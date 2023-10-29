import jwt
import datetime
from typing import Annotated
from fastapi import Header, HTTPException


async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")


async def make_token(secret_key, user_id, expiration_minutes=60):
    # Tentukan payload (klaim) untuk token
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow()
        + datetime.timedelta(minutes=expiration_minutes),
    }

    # Buat token menggunakan PyJWT
    token = jwt.encode(payload, secret_key, algorithm="HS256")

    return token
