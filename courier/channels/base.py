from mypy_boto3_sqs import ServiceResource
from typing import Tuple, List
import json

import logging
from abc import ABC
from .. import schemas


FailedMessage = schemas.Message
SuccessfulMessage = schemas.Message
DeliveryResults = Tuple[List[SuccessfulMessage], List[FailedMessage]]


class DeliveryError(Exception):
    pass


class Channel(ABC):
    def deliver(self, message: schemas.Message):
        ...

    def deliver_batch(self, messages: List[schemas.Message]) -> DeliveryResults:
        ...

    def receive(self):
        ...


class SqsChannel(Channel):
    SQS_BATCH_LIMIT = 10

    def __init__(self, sqs_resource: ServiceResource):
        self._sqs_resource = sqs_resource

    def deliver(self, message: schemas.Message):
        try:
            queue = self._sqs_resource.get_queue_by_name(QueueName=message.destination)
            _ = queue.send_message(MessageBody=json.dumps(message.body))
        except Exception as error:
            logging.exception(
                f"Message {message.id_} could not be delivered: ", exc_info=error
            )
            raise DeliveryError(error)

    def deliver_batch(self, messages: List[schemas.Message]) -> DeliveryResults:
        succeeded = []
        failed = []
        for message in messages:
            try:
                self.deliver(message)
                succeeded.append(message)
            except DeliveryError:
                failed.append(message)
        return succeeded, failed

    def receive(self):
        queue = self._sqs_resource.get_queue_by_name(QueueName="string")
        messages = queue.receive_messages()
        logging.info(messages)
        # TODO: cast to schema
        return messages


class RedisChannel(ABC):
    ...
