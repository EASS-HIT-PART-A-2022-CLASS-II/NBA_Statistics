FROM python:3.8

WORKDIR /app/src
WORKDIR /app

COPY . /app/src
COPY ./requierments.txt /app

RUN pip install -r requierments.txt
EXPOSE  8080

CMD ["streamlit", "run", "frontend.py"]
