# Meeting Summary & Action Plan Generator

A modular, microservice-based system to automatically generate summaries and action plans from meeting transcripts. Users can upload `.txt` or `.pdf` files, and the system processes the transcript through dedicated services to produce structured outputs.

---

## Architecture Overview

This project is built using **FastAPI** and **Streamlit**, structured into independent microservices:

```
microservice_app/
│
├── upload_service/       # Handles .txt/.pdf file parsing
├── summarizer_service/   # Generates summaries from transcript using Transformers
├── planner_service/      # Creates action plans from summary
├── frontend/             # Streamlit interface for users
├── shared/               # (Optional) Shared utilities or models
├── docker-compose.yml    # Orchestration for all services
├── run_tests.py          # Benchmark script for latency and throughput
├── test_services.ps1     # PowerShell health-check script
└── requirements.txt
```

---

## How It Works

1. **Upload Service (Port 8000)**  
   Parses `.txt` or `.pdf` and extracts raw text.

2. **Summarizer Service (Port 8001)**  
   Uses T5 or GPT-like model via HuggingFace to summarize the transcript.

3. **Planner Service (Port 8002)**  
   Converts the summary into an actionable task list using prompt-based logic.

4. **Frontend (Port 8501)**  
   Simple Streamlit UI for uploading, viewing summary, and getting action plan.

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/rishabhjohri/Meeting-Summary-Action-Plan-Generator.git
cd Meeting-Summary-Action-Plan-Generator/microservice_app
```

### 2. Build & Run with Docker Compose

```bash
docker-compose up --build
```

This will start all 4 services.

---

## Test All Services

Run this PowerShell script to verify all services are up:

```powershell
./test_services.ps1
```

Expected output:
```
Upload API is UP at http://localhost:8000/docs
Summarizer API is UP at http://localhost:8001/docs
Planner API is UP at http://localhost:8002/docs
Frontend is UP at http://localhost:8501
```

---

## Benchmark Latency & Throughput

Use the `run_tests.py` script to benchmark latency and throughput by sending 10 sample `.txt` files:

```bash
python run_tests.py
```

Sample output:
```
Sending 10 test files to Upload Service...
✅ test1.txt uploaded successfully | Latency: 2040.54 ms
...
Average Latency: 2040.62 ms
Throughput: 0.49 req/sec
```

---

## Access Points

| Service         | URL                            |
|----------------|---------------------------------|
| Upload API     | http://localhost:8000/docs      |
| Summarizer API | http://localhost:8001/docs      |
| Planner API    | http://localhost:8002/docs      |
| Frontend       | http://localhost:8501           |

---

## Example Output

**Input Transcript (Uploaded):**
```
Alice: Let's get started. Bob, any update on client feedback?
Bob: Yes, they want a more responsive dashboard with dark mode.
Clara: I’ll refactor the frontend components this week.
```

**Summary:**
```
Client wants a more responsive dashboard and dark mode.
Clara will refactor the frontend this week.
```

**Action Plan:**
```
Clara: Refactor frontend components by Friday.
Bob: Monitor client feedback integration.
```

---

## Built With

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Streamlit](https://streamlit.io/)
- [Transformers](https://huggingface.co/transformers/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## Author

Rishabh Johri | [GitHub](https://github.com/rishabhjohri)

---

