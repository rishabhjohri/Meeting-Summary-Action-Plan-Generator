Write-Host "🚀 Starting Upload Service on port 8000..."
Start-Process powershell -ArgumentList 'cd upload_service; uvicorn main:app --reload --port 8000'

Start-Sleep -Seconds 2

Write-Host "🚀 Starting Summarizer Service on port 8001..."
Start-Process powershell -ArgumentList 'cd summarizer_service; uvicorn main:app --reload --port 8001'

Start-Sleep -Seconds 2

Write-Host "🚀 Starting Planner Service on port 8002..."
Start-Process powershell -ArgumentList 'cd planner_service; uvicorn main:app --reload --port 8002'

Start-Sleep -Seconds 2

Write-Host "🌐 Launching Streamlit Frontend..."
Start-Process powershell -ArgumentList 'cd frontend; streamlit run app.py'

Write-Host "✅ All services and frontend started."
