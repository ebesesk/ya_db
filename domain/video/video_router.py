from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session


from database import get_db
from .video_crud import get_all_videos, get_video_list
from .video_schema import VideoItem, VideoItemsList
# from models import Video
# from db.repository.users import create_new_user

router =APIRouter()

@router.get("/all", response_model=list[VideoItem])
def view_all(db: Session=Depends(get_db)):
    videos = get_all_videos(db)
    return videos


@router.get("/list", response_model=VideoItemsList)
def get_list(db: Session = Depends(get_db),
                   page: int = 0,
                   size: int = 10):
    total, video_list = get_video_list(db=db, skip=page*size, limit=size)
    # manga_list = []
    # for manga in _manga_list:
    #     images = manga_util.get_images(manga.title)
    #     manga_list.append({'id': manga.id,'title': manga.title,'tag': manga.tag,'created_date': manga.created_date, 'images': images})
        
    return {
        'total': total,
        'video_list': video_list
    }