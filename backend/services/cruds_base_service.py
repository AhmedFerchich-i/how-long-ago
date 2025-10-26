
from typing import TypeVar,Generic,List,Type
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select,update,func
from pydantic import BaseModel
import uuid
CreateSchemaType=TypeVar("CreateSchemaType",bound=BaseModel)
PatchSchemaType=TypeVar("PatchSchemaType",bound=BaseModel)

ModelType=TypeVar("ModelType",bound=DeclarativeBase)
class CrudsBaseService(Generic[ModelType,CreateSchemaType,PatchSchemaType]):

    def __init__(self,model:Type[ModelType]):
        self.model=model
        

    async def create(self,data:CreateSchemaType,db:AsyncSession)->ModelType:
        obj=self.model(**data.model_dump())
        db.add(obj)
        await db.commit()
        await db.refresh(obj)
        return obj

    async def delete_by_id(self,id:uuid.UUID,db:AsyncSession)->ModelType|None:
        obj= await db.get(self.model,id)
        if obj :
            await db.delete(obj)
            await db.commit()
            return obj
        return None
    async def read_by_id(self,id:uuid.UUID,db:AsyncSession)->ModelType:
        obj= await db.get(self.model,id)
        if obj :
            return obj
        return None

    async def read_all(self,limit:int,offset:int,db:AsyncSession)->List[ModelType]:
        total_stmt=select(func.count()).select_from(self.model)
        total_result=await db.execute(total_stmt)
        total= total_result.scalar_one()
        stmt=select(self.model).offset(offset).limit(limit)
        result= await db.execute(stmt)
        items=result.scalars().all()
        return  {
        "total": total,
        "limit": limit,
        "offset": offset,
        "items": items
    }
    async def patch_by_id(self,id:uuid.UUID,data:PatchSchemaType,db:AsyncSession)->ModelType|None:
        obj= await db.get(self.model,id)
        if obj :
           
           stmt=update(self.model).where(self.model.id==id).values(**data.model_dump(exclude_unset=True))
           await db.execute(stmt)
           await db.commit()
           await db.refresh(obj)
           return obj
        return None