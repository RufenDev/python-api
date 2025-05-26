from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from env import envs
from api.routes import router as api_routes

API_PREFIX = "/api/v1"

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=envs.CORS_ORIGINS,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(api_routes, prefix=API_PREFIX)
