from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.db import get_db
from services.event_crud_service import get_event_crud_service
from services.cruds_base_service import CrudsBaseService
from schemas.event_schemas import (
    CreateEventSchema,
    PatchEventSchema,
    ReadEventSchema,
    GetEventsSchema,
)
from models.event import Event
import uuid

router = APIRouter(prefix="/events", tags=["Events"])


@router.post("/", response_model=ReadEventSchema)
async def create_event(
    data: CreateEventSchema,
    db: AsyncSession = Depends(get_db),
    service: CrudsBaseService[Event, CreateEventSchema, PatchEventSchema] = Depends(get_event_crud_service),
):
    event = await service.create(data, db)
    return event


@router.get("/", response_model=GetEventsSchema)
async def get_all_events(
    limit: int = 10,
    offset: int = 0,
    db: AsyncSession = Depends(get_db),
    service: CrudsBaseService[Event, CreateEventSchema, PatchEventSchema] = Depends(get_event_crud_service),
):
    response = await service.read_all(limit, offset, db)
    # the service already returns dict with {total, limit, offset, items}
    # but our schema expects {total, limit, offset, users/items}
    return response


@router.get("/{event_id}", response_model=ReadEventSchema)
async def get_event_by_id(
    event_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    service: CrudsBaseService[Event, CreateEventSchema, PatchEventSchema] = Depends(get_event_crud_service),
):
    event = await service.read_by_id(event_id, db)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@router.patch("/{event_id}", response_model=ReadEventSchema)
async def patch_event(
    event_id: uuid.UUID,
    data: PatchEventSchema,
    db: AsyncSession = Depends(get_db),
    service: CrudsBaseService[Event, CreateEventSchema, PatchEventSchema] = Depends(get_event_crud_service),
):
    event = await service.patch_by_id(event_id, data, db)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@router.delete("/{event_id}")
async def delete_event(
    event_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    service: CrudsBaseService[Event, CreateEventSchema, PatchEventSchema] = Depends(get_event_crud_service),
):
    deleted_event = await service.delete_by_id(event_id, db)
    if not deleted_event:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"detail": "Event deleted successfully"}
