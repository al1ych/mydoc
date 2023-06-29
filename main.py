# python3 -m uvicorn main:app --reload 

import json

from fastapi import FastAPI, Body
from fastapi.openapi.utils import get_openapi
from fastapi.responses import HTMLResponse
from starlette.responses import FileResponse, JSONResponse
from starlette.staticfiles import StaticFiles

from models import UserModel
from meta_config import *

app = FastAPI(
    title=app_title,
    description=app_desc,
    version=app_version,
    redoc_url=None,
    docs_url=app_docs,
    openapi_url=app_openapi,
    openapi_tags=app_tags,
)

# this is for mts logo to work (and also any other static you want)
app.mount("/static", StaticFiles(directory="static"), name="static")


method_translations = {
    "GET": "Получить",
    "POST": "Добавить",
    "PUT": "Обновить",
    "DELETE": "Удалить",
}

users = []


def custom_openapi():
    openapi_schema = get_openapi(
        title=app_title,
        version=app_version,
        description=app_desc,
        routes=app.routes,
        tags=app_tags,
    )

    # Translate method names
    for path, methods in openapi_schema["paths"].items():
        for method, operation in methods.items():
            # translate request's method to russian
            pass

    return openapi_schema


app.openapi = custom_openapi


# get request for mydoc.html
@app.get("/mydoc", response_class=HTMLResponse, include_in_schema=False)
async def custom_mydoc():
    html_file = open("static/mydoc.html", "r")
    html_content = html_file.read()
    html_file.close()
    return HTMLResponse(content=html_content)


# endpoints start here

# get image
@app.get("/image", tags=["Image"],
         summary="Get image",
         operation_id="get_image")
async def get_image():
    return FileResponse("static/mts_logo.png")
  
@app.get("/users", tags=["Users"],
         summary="Get users",
         operation_id="get_all_users")
async def get_users():
    return {"users": users}


@app.get("/users/{id}",
         response_model=UserModel,
         tags=["Users"],
         summary="Get user by ID",
         operation_id="get_user_by_id")
async def get_user(id: int):
    return UserModel(name="User1", id=id)


@app.post("/users", tags=["Users"],
          summary="Add a new user",
          operation_id="add_new_user")
async def add_user(name: str = Body(...)):
    users.append(name)
    return {"message": f"add 1 user ({name})"}


@app.delete("/users/{name}", tags=["Users"],
            summary="Delete a user by Name",
            operation_id="delete_user_by_name")
async def delete_user(name: str):
    print("name", name)
    users.remove(name)
    return {"message": f"deleted {name}"}


@app.put("/users/{id}/{newName}", tags=["Users"],
         summary="Update user by ID",
         operation_id="update_user_by_id")
async def update_user(id: int, newName: str):
    users[id] = newName
    return {"message": f"updated {id} to {newName}"}


@app.get("/things", tags=["Things"],
         summary="Get all things",
         operation_id="get_all_things")
async def get_things():
    return {"things": [1, 2, 3, "String!"]}



@app.get("/things2", tags=["Things"],
         summary="Get all things 2",
         operation_id="get_all_things_2")
async def get_things():
    return {"things": [1, 2, 3, "String!"]}


@app.get("/table")
async def get_table_data():
    data = [
        {"column1": "Row1 Col1", "column2": 1},
        {"column1": "Row2 Col1", "column2": 2},
        {"column1": "Row3 Col1", "column2": 3},
    ]
    table_response = {
        "type": "table",
        "data": data,
    }
    return JSONResponse(content=table_response)