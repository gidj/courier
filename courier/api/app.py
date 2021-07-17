from typing import List
from fastapi import FastAPI, status
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from courier.database import SessionLocal

from courier.repository import messages as message_repository
from courier import schemas

app = FastAPI()


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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
    message_dict = db_message.__dict__
    print(message_dict)
    return schemas.Message(**message_dict)


@app.get("/messages/", response_model=List[schemas.Message])
def read_messages(db: Session = Depends(get_db)):
    messages = message_repository.get_list(db)
    return messages
