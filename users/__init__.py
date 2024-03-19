from pydantic import BaseModel


# Валидатор для регистрации
class RegisterValidator(BaseModel):
    username: str
    surname: str
    phone_number: str
    city: str
    password: str


# Валидатор для логина
class EditUserValidator(BaseModel):
    user_id: int
    edit_info: str
    new_info: str
