
from .cruds_base_service import CrudsBaseService
from schemas.user_schemas import CreateUserSchema,PatchUserSchema
from models.user import User


def get_user_crud_service() -> CrudsBaseService[User, CreateUserSchema, PatchUserSchema]:
    return CrudsBaseService(User)