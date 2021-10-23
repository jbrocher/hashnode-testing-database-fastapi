from sqlalchemy import select
from sqlalchemy.orm import Session

from . import schemas
from .models import Item


def get_items(db: Session):
    items = select(Item)
    return db.execute(items).scalars().all()


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
