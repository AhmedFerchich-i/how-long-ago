from .cruds_base_service import CrudsBaseService
from schemas.event_schemas import CreateEventSchema,PatchEventSchema
from models.event import Event

def get_event_crud_service() -> CrudsBaseService[Event,CreateEventSchema,PatchEventSchema]:
    return CrudsBaseService(Event)