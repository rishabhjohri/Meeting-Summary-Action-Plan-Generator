FROM python:3.13-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir fastapi uvicorn PyPDF2 python-multipart

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
