from typing import List
from fastapi import FastAPI, status
from fastapi.param_functions import Depends
from pydantic.main import BaseModel
from sqlalchemy.orm.session import Session
from courier.database import SessionLocal
from ..sqs import get_sqs_resource, ServiceResource
from ..services.messages import DeliveryService

from ..channels import SqsChannel
from courier.repository import messages as message_repository
from courier import schemas

app = FastAPI()


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_sqs() -> ServiceResource:
    return get_sqs_resource()


@app.post(
    "/messages/", status_code=status.HTTP_201_CREATED, response_model=schemas.Message
)
def create_message(
    message: schemas.MessageCreate, db: Session = Depends(get_db)
) -> schemas.Message:
    db_message = message_repository.create(
        db,
        message.type_,
        message.body,
        message.destination,
        message.deliver_after,
    )
    return db_message


@app.get("/messages/", response_model=List[schemas.Message])
def read_messages(db: Session = Depends(get_db)):
    messages = message_repository.get_list(db)
    return messages


@app.post("/messages/deliver")
def deliver_messages(
    db: Session = Depends(get_db), sqs: ServiceResource = Depends(get_sqs)
):
    sqs_channel = SqsChannel(sqs)
    deliver_service = DeliveryService(db, sqs_channel)
    succeeded, failed = deliver_service.dispatch(10)
    return {"succeeded": succeeded, "failed": failed}


@app.get("/messages/receive")
def deliver_messages(
    db: Session = Depends(get_db), sqs: ServiceResource = Depends(get_sqs)
):
    sqs_channel = SqsChannel(sqs)
    messages = sqs_channel.receive()
    sqs_messages = [
        (
            message.body,
            message.message_id,
            message.queue_url,
            message.attributes,
            message.message_attributes,
        )
        for message in messages
    ]
    return {"messages": sqs_messages}
