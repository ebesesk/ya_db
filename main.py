from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


from domain import base_router 


app = FastAPI()

# origins = ["http://192.168.0.43:7443","http://191.168.0.43:7080"]
origins = ["http://192.168.0.43:7443"]
origins = []

app.add_middleware(
    CORSMiddleware,
    # allow_origins = ["*"],
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(base_router.router)