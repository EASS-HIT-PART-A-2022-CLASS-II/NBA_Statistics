FROM python:3.8
WORKDIR /app/src
WORKDIR /app

COPY ./src  /app/src
COPY ./requierments.txt /app
WORKDIR /app
RUN pip install -r requierments.txt
EXPOSE  8080

CMD ["uvicorn","src.main:app","--host=0.0.0.0","--reload"]

