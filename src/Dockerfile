FROM python:3.8
WORKDIR /app/src
WORKDIR /app

COPY . /app/src
COPY ./requierments.txt /app

RUN pip install -r requierments.txt
EXPOSE  2375

CMD ["uvicorn","src.main:app","--host=0.0.0.0","--reload"]

