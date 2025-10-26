from fastapi import APIRouter,Depends,HTTPException,status
from services.user_crud_service import get_user_crud_service
from core.db import get_db
from schemas.user_schemas import GetUsersResponseSchema,ReadUserSchema,CreateUserSchema,PatchUserSchema
from services.cruds_base_service import CrudsBaseService
from sqlalchemy.ext.asyncio import AsyncSession
from models.user import User
from utils.password import hash_password
router=APIRouter(prefix='/users')

@router.get('/',response_model=GetUsersResponseSchema)
async def get_all_users(limit:int=10,offset:int=0,db=Depends(get_db),service:CrudsBaseService=Depends(get_user_crud_service)):
    response= await service.read_all(limit,offset,db=db)
    return response


@router.get("/{user_id}", response_model=ReadUserSchema)
async def get_user_by_id(
    user_id: str,
    db: AsyncSession = Depends(get_db),
    service: CrudsBaseService[User, CreateUserSchema, PatchUserSchema] = Depends(get_user_crud_service)
):
    """Get user by ID"""
    user = await service.read_by_id(user_id, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.post("/", response_model=ReadUserSchema, status_code=status.HTTP_201_CREATED)
async def create_user(
    data: CreateUserSchema,
    db: AsyncSession = Depends(get_db),
    service: CrudsBaseService[User, CreateUserSchema, PatchUserSchema] = Depends(get_user_crud_service)
):
    """Create a new user"""
    data.password=hash_password(data.password)
    user = await service.create(data, db)
    return user


@router.patch("/{user_id}", response_model=ReadUserSchema)
async def update_user(
    user_id: str,
    data: PatchUserSchema,
    db: AsyncSession = Depends(get_db),
    service: CrudsBaseService[User, CreateUserSchema, PatchUserSchema] = Depends(get_user_crud_service)
):
    """Update a user by ID"""
    user = await service.patch_by_id(user_id, data, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.delete("/{user_id}", response_model=ReadUserSchema)
async def delete_user(
    user_id: str,
    db: AsyncSession = Depends(get_db),
    service: CrudsBaseService[User, CreateUserSchema, PatchUserSchema] = Depends(get_user_crud_service)
):
    """Delete a user by ID"""
    user = await service.delete_by_id(user_id, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user