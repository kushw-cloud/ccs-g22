import streamlit as st
import requests

st.title("🇮🇳 Indian Cyber Threat Monitoring")

response = requests.get("http://localhost:8000/incidents")
data = response.json()

for incident in data["incidents"]:
    st.write(f"**{incident['type']}** - {incident['details']}")

