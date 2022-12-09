FROM python:3.8
COPY ./src  /app/src
COPY ./requierments.txt /app
WORKDIR /app
RUN pip install -r requierments.txt
EXPOSE  8000

CMD ["uvicorn","main:app","--host=0.0.0.0","--reload"]

