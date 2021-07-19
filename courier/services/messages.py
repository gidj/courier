from datetime import datetime
from typing import Tuple
from .. import schemas
from sqlalchemy.orm.session import Session
from ..repository import messages as message_repository

from ..channels import Channel


class DeliveryService:
    def __init__(self, db: Session, channel: Channel):
        self._db = db
        self._channel = channel

    def dispatch(self, limit=100) -> Tuple:
        self._db.begin()
        messages = message_repository.get_list_with_update(
            self._db, datetime.utcnow(), limit=limit
        )
        _messages = [schemas.Message.from_orm(message) for message in messages]
        succeeded, failed = self._channel.deliver_batch(_messages)
        if succeeded:
            message_repository.delete(self._db, [message.id_ for message in succeeded])
        self._db.commit()
        return succeeded, failed
