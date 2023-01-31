from datetime import datetime
from pydantic import BaseModel
from typing import Union, Optional
from datetime import date
from typing import List



class VideoItem(BaseModel):
    id: int
    dbid: str
    width: int | None = None
    height: int | None = None
    showtime: int | None = None
    bitrate: int | None = None
    filesize: int | None = None
    cdate: date | None = None
    
    display_quality: str | None = None
    country: str | None = None
    face: str | None = None
    look: str | None = None
    age: str | None = None
    pussy: str | None = None

    etc: str | None = None

    school_uniform: bool | None = None
    hip: bool | None = None
    group: bool | None = None
    pregnant: bool | None = None
    conversation: bool | None = None
    lesbian: bool | None = None
    ani: bool | None = None
    oral: bool | None = None
    masturbation: bool | None = None
    massage: bool | None = None
    uniform: bool | None = None
    family: bool | None = None
    
    ad_start: int | None = None
    ad_finish: int | None = None
    star: int | None = None
    
    date_posted: date | None = None
    date_modified: date | None = None

    class Config:
        orm_mode = True

class VideoItemsList(BaseModel):
    total: int
    video_list: list[VideoItem] = []
    
# class VideoItems(BaseModel):
#     Video_list: list[VideoItem] = []