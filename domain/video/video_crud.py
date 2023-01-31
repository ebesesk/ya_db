from sqlalchemy.orm import Session
from models import Video



def get_all_videos(db: Session):
    # print(db.query(Video).all())
    return db.query(Video).all()

def get_video_list(db: Session, skip:int=0, limit:int=0):
    _video_list = db.query(Video).order_by(Video.date_posted.desc())
    total = _video_list.count()
    video_list = _video_list.offset(skip).limit(limit).all()
    return total, video_list

# def get_all_mangas(db: Session):
#     return db.query(Manga).all()