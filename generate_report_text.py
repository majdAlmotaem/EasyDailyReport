import requests
from config import HUGGINGFACE_API_KEY

API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

def generate_report_text(activities):
    report = {}
    
    for day, activity in activities.items():
        payload = {
            "inputs": f"Formuliere diesen Stichpunkt in einen vollständigen Satz: {activity}"
        }
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        
        generated_text = response.json()[0]['generated_text'].strip()
        report[day] = f"Am {day} habe ich {generated_text}"
    
    return report