# there will be 7 types of api classes
# 1. chat apis
# 2. learning apis
# 3. user login apis
# 4. database apis
# 5. others as per need

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database.database_main import Base
from .database.database_main import engine

from .api_routes import auth

app = FastAPI()

origins = ["http://localhost:2222"]

app.include_router(auth.auth_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Hello World"}