from pydantic import BaseModel


class Outfit(BaseModel):
    id: str
    link: str
    submitter: str
    discord_name: str
    tag: str
    meta: str | None = None
    created: str
    updated: str
    deleted: bool = False
    featured: bool = False
    display_count: int = 0
    delete_hash: str
