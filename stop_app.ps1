Write-Host "🛑 Stopping all running uvicorn services..."
Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -like "*uvicorn*" } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }

Write-Host "🛑 Stopping streamlit frontend..."
Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -like "*streamlit run*" } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }

Write-Host "✅ All services and frontend have been stopped."
