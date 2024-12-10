from fastapi import FastAPI, Path
from fastapi.responses import HTMLResponse
from typing import Annotated
from pydantic import constr, conint

app = FastAPI()

# Изначальный словарь пользователей
users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_users():
    return users

@app.post("/user/{username}/{age}")
async def create_user(
    username: Annotated[constr(min_length=5, max_length=20), Path(description="Enter username")],
    age: Annotated[conint(ge=18, le=120), Path(description="Enter age")]
):
    user_id = str(max(map(int, users.keys())) + 1)  # Генерация нового user_id
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
    user_id: Annotated[conint(ge=1), Path(description="Enter User ID")],
    username: Annotated[constr(min_length=5, max_length=20), Path(description="Enter username")],
    age: Annotated[conint(ge=18, le=120), Path(description="Enter age")]
):
    if str(user_id) not in users:
        return {"error": "User not found"}
    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} has been updated"

@app.delete("/user/{user_id}")
async def delete_user(
    user_id: Annotated[conint(ge=1), Path(description="Enter User ID")]
):
    if str(user_id) in users:
        del users[str(user_id)]
        return f"User {user_id} has been deleted"
    return {"error": "User not found"}



DELETE /user/2


GET /users