FROM python:3.10-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["gunicorn", "main:app", "-b", "0.0.0.0:8080"]
