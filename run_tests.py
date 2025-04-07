import time
import requests
import os

#UPLOAD_URL = "http://<external-ip>:8000/upload/"  # Replace with actual public IP of your GCP VM
UPLOAD_URL = "http://localhost:8000/upload/"  # For local testing

test_dir = "test_files"
test_files = [f for f in os.listdir(test_dir) if f.endswith(".txt")]
latencies = []

print(f"📤 Sending {len(test_files)} test files to Upload Service...\n")

for file in test_files:
    file_path = os.path.join(test_dir, file)
    with open(file_path, "rb") as f:
        files = {"file": (file, f, "text/plain")}
        start = time.time()
        response = requests.post(UPLOAD_URL, files=files)
        end = time.time()

        latency_ms = (end - start) * 1000
        latencies.append(latency_ms)

        if response.status_code == 200:
            print(f"✅ {file} uploaded successfully | Latency: {latency_ms:.2f} ms")
        else:
            print(f"❌ {file} failed | Status Code: {response.status_code}")

# Metrics
avg_latency = sum(latencies) / len(latencies)
throughput = len(latencies) / (sum(latencies) / 1000)

print("\n📊 Benchmark Results:")
print(f"Average Latency: {avg_latency:.2f} ms")
print(f"Throughput: {throughput:.2f} req/sec")
