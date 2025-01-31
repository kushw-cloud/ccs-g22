from fastapi import FastAPI
from db import insert_incident, get_incidents
from fetch_data import fetch_threats

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Cyber Incident Monitoring API"}

@app.get("/incidents")
def get_live_incidents():
    return {"incidents": get_incidents()}

@app.get("/fetch")
def fetch_latest():
    data = fetch_threats()
    return {"status": "Data fetched", "new_incidents": data}
