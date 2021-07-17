FROM python:3.9

WORKDIR /src/app

COPY ./requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

COPY ./courier ./courier

CMD ["uvicorn", "courier.api.app:app", "--host", "0.0.0.0", "--port", "8000"]
