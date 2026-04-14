from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response
import time
import random

app = FastAPI()

# Metrics
REQUEST_COUNT = Counter("request_count", "Total requests")
ERROR_COUNT = Counter("error_count", "Total errors")

@app.get("/")
def home():
    REQUEST_COUNT.inc()
    time.sleep(random.uniform(0.1, 0.5))  # simulate latency
    return {"message": "Monitoring Stack Running 🚀"}

@app.get("/error")
def error():
    REQUEST_COUNT.inc()
    ERROR_COUNT.inc()
    return {"error": "Something went wrong"}, 500

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")