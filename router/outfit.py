from fastapi import APIRouter, Depends

from fs_types.outfit import Outfit
from auth.validate_token_header import validate_token

router = APIRouter(
    prefix="/outfits",
    tags=["outfits"],
    dependencies=[Depends(validate_token)],
    responses={404: {"description": "Not Found"}}
)


@router.get("/")
async def read_outfits():
    # Return all outfits, ordered, paginated
    return ""


@router.get("/{outfit_id}")
async def read_outfit(outfit_id: str):
    # Return the one outfit
    return {"outfit_id": outfit_id}


@router.get("/search")
async def search_outfits():
    return ""
    # This one will use the request body to pass search parameters


@router.post("/")
async def create_outfit(outfit: Outfit):
    return outfit
