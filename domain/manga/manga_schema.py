import datetime
from pydantic import BaseModel, validator, EmailStr
from typing import List, Optional

class Manga(BaseModel):
    id: int
    title: str
    tag: str | None = None
    created_date: datetime.datetime | None = None
    images: List[str]
    
    
class MangaList(BaseModel):
    total: int = 0
    manga_list: List[Manga] = []