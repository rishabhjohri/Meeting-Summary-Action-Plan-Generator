#!/bin/bash

echo "---- METRICS COLLECTION ----"

# 1. Start Boot Time Tracking
START=$(date +%s)

echo "Waiting for frontend (Streamlit) to become available..."
until curl -s --max-time 2 http://localhost:8501 > /dev/null; do
    sleep 1
done

END=$(date +%s)
BOOT_TIME=$((END - START))
echo "Boot Time: $BOOT_TIME seconds"

# 2. CPU & RAM Usage Snapshot from Docker containers
echo "Capturing Docker Stats..."
docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}" > docker_stats.txt
cat docker_stats.txt

# 3. Run Benchmark (Assumes test_files & run_tests.py are already on VM)
echo "Running Benchmark Tests..."
python3 run_tests.py > benchmark_output.txt
cat benchmark_output.txt

# 4. Extract metrics and save to a unified log
LATENCY=$(grep "Average Latency" benchmark_output.txt | awk '{print $3}')
THROUGHPUT=$(grep "Throughput" benchmark_output.txt | awk '{print $2}')

cat <<EOF > performance_summary.log
BOOT TIME (sec): $BOOT_TIME
AVERAGE LATENCY (ms): $LATENCY
THROUGHPUT (req/sec): $THROUGHPUT

--- DOCKER RESOURCE USAGE ---
$(cat docker_stats.txt)
EOF

echo "All metrics saved to performance_summary.log"
