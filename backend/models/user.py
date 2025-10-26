
from core.db import Base
import uuid
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import types,String
from typing import List
from mixins.time_stamp import TimeStampMixin
class User(Base,TimeStampMixin):
    __tablename__="users"
    id:Mapped[uuid.UUID]=mapped_column(types.Uuid,primary_key=True,default=uuid.uuid4)
    name:Mapped[str]=mapped_column(String(50),nullable=False)
    password:Mapped[str]=mapped_column(String,nullable=True)
    email:Mapped[str]=mapped_column(String(100),nullable=False,unique=True)
    events:Mapped[List["Event"]]=relationship("Event",back_populates="user")