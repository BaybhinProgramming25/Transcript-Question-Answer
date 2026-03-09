from pydantic import BaseModel, Field

class LoginData(BaseModel):
    email: str = Field(min_length=10, max_length=50)
    password: str = Field(min_length=8, max_length=20)

class SignUpData(BaseModel):
    firstname: str = Field(min_length=1, max_length=100)
    lastname: str = Field(min_length=1, max_length=100)
    email: str = Field(min_length=10, max_length=50)
    password: str = Field(min_length=8, max_length=20)

