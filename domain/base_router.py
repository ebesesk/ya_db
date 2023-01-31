from fastapi import APIRouter
from .login import login_router
from .users import users_router
from .manga import manga_router
from .video import video_router

router = APIRouter()

router.include_router(login_router.router, prefix="/api/login", tags=["login"])
router.include_router(users_router.router, prefix="/api/users", tags=["users"])
router.include_router(manga_router.router, prefix="/api/manga", tags=["manga"])
router.include_router(video_router.router, prefix="/api/video", tags=["video"])