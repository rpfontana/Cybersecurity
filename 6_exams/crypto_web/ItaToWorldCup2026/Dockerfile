FROM python:3.9-slim

WORKDIR /app

RUN pip install flask

COPY webapp/ /app/

RUN python db_init.py

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask", "run"]
