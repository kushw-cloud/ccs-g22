import schedule
import time
import subprocess

def fetch_data():
    print("Fetching new cyber incidents...")
    subprocess.run(["python", "fetch_data.py"])

# Run every 10 minutes
schedule.every(10).minutes.do(fetch_data)

while True:
    schedule.run_pending()
    time.sleep(1)
