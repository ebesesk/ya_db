import datetime, os
from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from sqlalchemy.orm import Session
from typing import List

from database import get_db

from ..login.login_router import get_current_user
from . import manga_schema
from .manga_crud import bulk_insert_mangas, get_all_mangas, delete_db_list, get_manga_list
from . import manga_util
from models import Manga

from config import settings


router = APIRouter()


@router.get("/refresh", response_model=List[manga_schema.Manga])
def manga_refresh(db: Session = Depends(get_db)):
    mangas_dir = manga_util.get_manga_list()
    mangas_db = get_all_mangas(db)
    manga_titles = [i.title for i in mangas_db]
    
    # 추가된 만화 DB 등록
    mangas_new = []
    for manga in mangas_dir:
        if manga['title'] not in manga_titles:
            mangas_new.append(manga)
    bulk_insert_mangas(db=db, mangas=mangas_new)
    
    # 삭제한 만화 DB 삭제
    mangas_empty = []
    for manga in mangas_db:
        if manga.title not in [i['title'] for i in mangas_dir]:
            mangas_empty.append(manga)
    delete_db_list(db=db, mangas=mangas_empty)
    
    return mangas_new


@router.get("/list", response_model=manga_schema.MangaList)
def get_list(db: Session = Depends(get_db),
                   page: int = 0,
                   size: int = 10):
    total, _manga_list = get_manga_list(db=db, skip=page*size, limit=size)
    manga_list = []
    for manga in _manga_list:
        images = manga_util.get_images(manga.title)
        manga_list.append({'id': manga.id,'title': manga.title,'tag': manga.tag,'created_date': manga.created_date, 'images': images})
        
    return {
        'total': total,
        'manga_list': manga_list
    }
 