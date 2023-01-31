import os, glob, shutil, datetime
from pathlib import Path

from models import Manga
from config import settings


# '/home/manga/CHANGE!!/config/workspace/manga/hdhd103'

MANGA_DIR = settings.MANGA_DIR

def get_manga_list():
    manga_list = [i for i in filter(os.path.isdir, glob.glob(MANGA_DIR + '/*'))]
    # manga_list = manga_list[0:101]
    
    manga_dict_list = []
    for i in manga_list:
        title = i[i.rfind('/')+1:]
        # page = len(os.listdir(i))
        created_date = datetime.datetime.now()
        manga_dict_list.append({'title':title, 'created_date': created_date})
        # manga_dict_list.append({'title':title, 'page':page, 'created_date': created_date})
    return manga_dict_list

def get_images(manga:str):
    images = []
    for i in os.listdir(settings.MANGA_DIR + '/' + manga):
        images.append(MANGA_DIR + '/' + i)
    return images