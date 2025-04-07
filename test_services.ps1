$services = @{
    "Upload API"     = "http://localhost:8000/docs"
    "Summarizer API" = "http://localhost:8001/docs"
    "Planner API"    = "http://localhost:8002/docs"
    "Frontend"       = "http://localhost:8501"
}

Write-Host "`n--- Testing Service URLs ---" -ForegroundColor Cyan

foreach ($name in $services.Keys) {
    $url = $services[$name]
    try {
        $response = Invoke-WebRequest -Uri $url -UseBasicParsing -TimeoutSec 5
        if ($response.StatusCode -eq 200) {
            Write-Host "$name is UP at $url" -ForegroundColor Green
        }
        else {
            Write-Host "$name is reachable but returned status code $($response.StatusCode)" -ForegroundColor Yellow
        }
    }
    catch {
        Write-Host "$name is DOWN or unreachable at $url" -ForegroundColor Red
    }
}

Write-Host "`n--- All checks complete ---" -ForegroundColor Cyan

