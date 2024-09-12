from pydantic import BaseModel


class SignUpModel(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str