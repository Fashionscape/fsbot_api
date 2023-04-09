from typing import Annotated
from fastapi import Header, HTTPException


async def validate_token(x_token: Annotated[str, Header()]):
    if x_token != "auth token here":
        raise HTTPException(status_code=400, detail="Invalid Token")

