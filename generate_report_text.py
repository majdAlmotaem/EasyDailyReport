import google.generativeai as genai

# Stellen Sie sicher, dass das Paket installiert ist:
# pip install google-generativeai
import time
import os
import logging
from config import API_KEY

# Suppress gRPC shutdown warning
os.environ['GRPC_PYTHON_LOG_LEVEL'] = 'error'
logging.getLogger('google.generativeai.generative_models').setLevel(logging.ERROR)

def generate_report_text(activities):
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    report = {}

    for day, activity in activities.items():
        prompt = f"Als Fachinformatiker-Azubi habe ich heute folgende Aufgaben erledigt: {activity}. Formuliere diese Stichpunkte in einem kurzen, prägnanten Satz (maximal 20 Wörter) für mein Berichtsheft."

        while True:
            try:
                response = model.generate_content(prompt)
                generated_text = response.text.strip()
                report[day] = f"Am {day} : {generated_text}"
                break

            except Exception as e:
                print(f"Ein Fehler ist aufgetreten: {e}")
                report[day] = f"Am {day} konnte der Text nicht generiert werden."
                break
    
    return report