from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    class Config:
        orm_mode= True
        schema_extra = {
            'example': {
                "username": "saurabh",
                "email": "saurabh@gmail.com",
                "password": "password",
                "is_staff": "False",
                "is_active": "True"
            }
        }


class Settings(BaseModel):
    authjwt_secret_key: str = 'ba0e5f7213a69664ca13f127f360090c7ce29317ec0b16b3cc8fe88fba11df84'


class LoginModel(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "username": "name",
                "password": "password"
            }
        }


class OrderModel(BaseModel):
    id: Optional[int]
    quantity: int
    order_status: Optional[str] = "PENDING"
    pizza_size: Optional[str] = "SMALL"
    user_id: Optional[int]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "quantity": 2,
                "pizza_size": "LARGE"
            }
        }


class OrderStatusModel(BaseModel):
    order_status: Optional[str]

    class Config:
        orm_mode: True
        schema_extra = {
            "example":{
                "order_status": "TRANSIT"
            }
        }
        