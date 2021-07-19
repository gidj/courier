import boto3
from mypy_boto3_sqs import ServiceResource
from ..settings import settings


def get_sqs_resource(
    region_name="us-west-2",
    endpoint_url=settings.SQS_ENDPOINT_URL,
) -> ServiceResource:
    sqs = boto3.resource(
        "sqs",
        region_name=region_name,
        endpoint_url=endpoint_url,
        aws_access_key_id="key",
        aws_secret_access_key="secret",
    )
    return sqs
