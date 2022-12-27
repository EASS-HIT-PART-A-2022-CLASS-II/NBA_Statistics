FROM python:3.8


WORKDIR /app/Frontend
WORKDIR /app

COPY . /app/Frontend

EXPOSE  8080

CMD streamlit run Frontend.py
