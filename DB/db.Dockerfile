FROM python:3.8


WORKDIR /app/DB

COPY . /app/DB

RUN pip install -r requierments.txt
RUN pip install pymongo
EXPOSE  27017

