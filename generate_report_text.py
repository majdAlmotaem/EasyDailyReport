import requests
from config import HUGGINGFACE_API_KEY

API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

def generate_report_text(activities):
    report = {}

    for day, activity in activities.items():
        payload = {
            "inputs": f"Als Fachinformatiker-Azubi habe ich heute folgende Aufgaben erledigt: {activity}. Formuliere diese Stichpunkte in einem vollständigen, professionellen Satz für mein Berichtsheft.",
            "parameters": {"temperature": 0.7, "max_new_tokens": 50, "return_full_text": False}
        }

        try:
            response = requests.post(API_URL, headers=headers, json=payload)
            response.raise_for_status()
            
            generated_text = response.json()[0]['generated_text'].strip()
            report[day] = f"Am {day} : {generated_text}"
        except requests.exceptions.RequestException as e:
            print(f"Ein Fehler ist aufgetreten: {e}")
            print(f"Antwort-Inhalt: {response.text}")
            report[day] = f"Am {day} konnte der Text nicht generiert werden."
    
    return report
