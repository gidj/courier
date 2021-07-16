from sqlalchemy.orm import Session
from uuid import UUID

from .. import models


def get(db: Session, message_id: UUID) -> models.Message:
    message = db.query(models.Message).filter(models.Message.id == message_id).first()
    return message
