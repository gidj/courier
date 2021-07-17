FROM python:3.9

WORKDIR /courier

COPY ./requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

COPY ./courier ./

CMD ["uvicorn", "courier.api.app:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
