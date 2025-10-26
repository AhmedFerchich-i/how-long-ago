from core.db import Base
import uuid
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import types,String,Date,Time,ForeignKey
from datetime import date,time
from mixins.time_stamp import TimeStampMixin
class Event(Base,TimeStampMixin):
    __tablename__="events"
    id:Mapped[uuid.UUID]=mapped_column(types.Uuid,primary_key=True,default=uuid.uuid4)
    title:Mapped[str]=mapped_column(String(100),nullable=False,index=True)
    description:Mapped[str]=mapped_column(String(5000),nullable=True)
    event_date:Mapped[date]=mapped_column(Date,nullable=False,index=True)
    event_time:Mapped[time]=mapped_column(Time,nullable=True,index=True)
    user_id:Mapped[uuid.UUID]=mapped_column(types.UUID,ForeignKey("users.id",ondelete="CASCADE"),nullable=False,index=True)
    user:Mapped["User"]=relationship("User",back_populates="events")