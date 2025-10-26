from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import DateTime
from datetime import datetime,timezone

class TimeStampMixin:
    created_at:Mapped[datetime]=mapped_column(DateTime,nullable=False,default=lambda : datetime.now())
    updated_at:Mapped[datetime]=mapped_column(DateTime,nullable=False,default=datetime.now,onupdate=datetime.now())