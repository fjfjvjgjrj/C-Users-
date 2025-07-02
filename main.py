from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials, OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

basic_auth = HTTPBasic()

# OAuth2 (без JWT, простий токен)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

users = {
    "admin": "admin123"
}

@app.get("/basic-protected")
def basic_protected(credentials: HTTPBasicCredentials = Depends(basic_auth)):
    correct_password = users.get(credentials.username)
    if not correct_password or correct_password != credentials.password:
        raise HTTPException(status_code=401, detail="Неправильні дані")
    return {"message": f"Привіт, {credentials.username}!"}

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password
    if users.get(username) != password:
        raise HTTPException(status_code=400, detail="Невірні логін або пароль")
    return {"access_token": f"token-for-{username}", "token_type": "bearer"}

@app.get("/oauth2-protected")
def oauth2_protected(token: str = Depends(oauth2_scheme)):
    if not token.startswith("token-for-"):
        raise HTTPException(status_code=401, detail="Недійсний токен")
    username = token.removeprefix("token-for-")
    return {"message": f"Ти авторизований як {username}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)