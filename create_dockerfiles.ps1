# upload_service
$upload = @"
FROM python:3.13-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir fastapi uvicorn PyPDF2

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
"@
$upload | Set-Content -Path "./upload_service/Dockerfile"

# summarizer_service
$summarizer = @"
FROM python:3.13-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir fastapi uvicorn transformers torch

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
"@
$summarizer | Set-Content -Path "./summarizer_service/Dockerfile"

# planner_service
$planner = @"
FROM python:3.13-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir fastapi uvicorn transformers torch

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]
"@
$planner | Set-Content -Path "./planner_service/Dockerfile"

# frontend
$frontend = @"
FROM python:3.13-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir streamlit requests

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
"@
$frontend | Set-Content -Path "./frontend/Dockerfile"

Write-Host "✅ All Dockerfiles created successfully!"
