FROM python:3.13-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir streamlit requests

EXPOSE 8501

#CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.enableCORS=false"]
