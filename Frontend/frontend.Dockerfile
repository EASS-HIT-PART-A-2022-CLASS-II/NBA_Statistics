FROM python:3.8


WORKDIR /app/Frontend

COPY . /app/Frontend

RUN pip install -r Frontend/requierments.txt
EXPOSE  8501

CMD streamlit run Frontend.py
