import uuid
from datetime import datetime

from sqlalchemy import TEXT, Column, DateTime
from sqlalchemy.dialects import postgresql

from ..database import Base


class Message(Base):
    __tablename__ = "messages"

    id: uuid.UUID = Column(
        postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    type_: str = Column(TEXT, nullable=False)
    body: dict = Column(postgresql.JSONB, nullable=False)
    destination: str = Column(TEXT, nullable=False)
    deliver_after: datetime = Column(DateTime, default=datetime.utcnow, nullable=False)
    created_at: datetime = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: datetime = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )
