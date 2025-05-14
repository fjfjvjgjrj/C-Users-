from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

user_names = []

class UserName(BaseModel):
    name: str

@app.post("/add")
async def add_user(user: UserName):
    if user.name in user_names:
        raise HTTPException(status_code=400, detail="Ім'я вже існує")
    user_names.append(user.name)
    return {"message": f"Ім'я '{user.name}' додано"}

@app.get("/users")
async def get_users():
    return {"users": user_names}

@app.delete("/delete")
async def delete_user(user: UserName):
    if user.name not in user_names:
        raise HTTPException(status_code=404, detail="Ім'я не знайдено")
    user_names.remove(user.name)
    return {"message": f"Ім'я '{user.name}' видалено"}

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=9000)

