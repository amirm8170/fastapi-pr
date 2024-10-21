from importlib import import_module
from fastapi import FastAPI, Request, HTTPException, status
from tortoise.contrib.fastapi import register_tortoise
import dotenv
import os
import routes

dotenv.load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

app = FastAPI()

register_tortoise(
    app,
    db_url=f'postgres://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}',
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True
)

for module_name in routes.__all__:
    module = import_module(f"routes.{module_name}")
    app.include_router(module.router)


@app.api_route("/{path_name:path}", methods=["GET", "POST"])
async def catch_all(_: Request, path_name: str):
    print(f'ERROR BAD REQUEST: {path_name}')
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
