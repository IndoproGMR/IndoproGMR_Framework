from pydantic import BaseModel


# base
class user_tableBase(BaseModel):
    name: str
    umur: int


# respond dari server
class user(user_tableBase):
    hidup: int
    id: int

    class Config:
        from_attributes = True


# respond dari pengguna
class user_update(user_tableBase):
    hidup: int


# Base Model
class data_user_tableBase(BaseModel):
    id_user: int


# resspond dari server
class data_user(user_tableBase):
    diskripsi: str

    class Config:
        from_attributes = True


# req dari user
class data_user_update(data_user_tableBase):
    diskripsi: str
