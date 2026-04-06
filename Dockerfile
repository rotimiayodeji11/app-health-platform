FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir flask gunicorn

EXPOSE 5001

CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:5001", "app:app"]