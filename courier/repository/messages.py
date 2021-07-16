from typing import List
from sqlalchemy.orm import Session
from uuid import UUID

from datetime import datetime
from .. import models


DELIVERY_LIMIT_DEFAULT = 100

def get_list(db: Session) -> List[models.Message]:
    messages = db.query(models.Message).all()
    return messages


def get_by_id(db: Session, message_id: UUID) -> models.Message:
    message = db.query(models.Message).filter(models.Message.id == message_id).first()
    return message


def create(
    db: Session,
    type_: str,
    body: dict,
    destination: str,
    deliver_after: datetime,
) -> models.Message:
    message = models.Message(
        type=type_, body=body, destination=destination, deliver_after=deliver_after
    )
    db.add(message)
    db.commit()
    db.refresh(message)
    return message


def get_list_with_update(
    db: Session, deliver_after: datetime = None, limit=DELIVERY_LIMIT_DEFAULT
) -> List[models.Message]:
    if not deliver_after:
        deliver_after = datetime.utcnow()
    messages = (
        db.query(models.Message)
        .filter(models.Message.deliver_after < deliver_after)
        .limit(limit)
        .with_for_update()
        .all()
    )
    return messages


def delete(db: Session, message_ids: List):
    db.query(models.Message).filter(models.Message.id.in_(message_ids)).delete()
    db.commit()
