from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    name: str
    lastname: str
    username: str
    country: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)