FROM python:3.8


WORKDIR /app/DB

COPY . /app/DB


RUN pip install pymongo


CMD ["python","icons.py"]