from pydantic import BaseModel
import uuid
from typing import Optional,List
from datetime import date,time,datetime

class CreateEventSchema(BaseModel):
    title:str
    description:Optional[str]=None
    event_date:date
    event_time:time
    user_id:uuid.UUID

class ReadEventSchema(BaseModel):
    id: uuid.UUID
    title: str
    description: Optional[str]
    event_date: date
    event_time: time
    user_id: uuid.UUID
    created_at:datetime
    updated_at:datetime

    class Config:
        from_attributes = True


class PatchEventSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    event_date: Optional[date] = None
    event_time: Optional[time] = None
    user_id: Optional[uuid.UUID] = None


class GetEventsSchema(BaseModel):
    offset: int
    total: int
    items: List[ReadEventSchema]