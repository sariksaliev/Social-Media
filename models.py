from pydantic import BaseModel


# Модель для логина
class LoginModel(BaseModel):
    username: str
    password: str


# Модель для регистрации
class RegisterModel(BaseModel):
    username: str
    email: str
    password: str


# Модель для токена (JWT)
class Token(BaseModel):
    access_token: str
    token_type: str