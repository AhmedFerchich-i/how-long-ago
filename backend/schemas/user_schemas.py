from pydantic import BaseModel
import uuid
from typing import Optional,List
from datetime import datetime
class CreateUserSchema(BaseModel):
    name:str
    email:str
    password:str
    

class ReadUserSchema(BaseModel):
    id:uuid.UUID
    name:str
    email:str
    created_at:datetime
    updated_at:datetime
    class Config:
        from_attributes=True


class PatchUserSchema(BaseModel):
    name:Optional[str]=None
    email:Optional[str]=None
    password:Optional[str]=None

class GetUsersResponseSchema(BaseModel):
    offset:int
    total:int
    limit:int
    items:List[ReadUserSchema]