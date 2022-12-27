FROM python:3.8


WORKDIR /app/Frontend

COPY . /app/Frontend

RUN pip install -r requierments.txt
EXPOSE  8080

CMD streamlit run Frontend.py
