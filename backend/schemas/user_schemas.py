from pydantic import BaseModel
import uuid
from typing import Optional,List

class CreateUserSchema(BaseModel):
    name:str
    email:str

class ReadUserSchema(BaseModel):
    id:uuid.UUID
    name:str
    email:str


class PatchUserSchema(BaseModel):
    name:Optional[str]=None
    email:Optional[str]=None

class GetUsersResponseSchema(BaseModel):
    offset:int
    total:int
    limit:int
    items:List[ReadUserSchema]