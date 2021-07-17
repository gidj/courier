from datetime import datetime
from sqlalchemy.orm.session import Session
from ..repository import messages as message_repository
from .. import schemas


def put_on_channel(message):
    pass

def deliver(db: Session, limit=100):
    db.begin()
    messages = message_repository.get_list_with_update(db, datetime.utcnow(), limit=limit)
    for message in messages:
        put_on_channel(message)
    pass
