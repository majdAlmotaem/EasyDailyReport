from openai import OpenAI
import time
from config import API_KEY

def generate_report_text(activities):
    client = OpenAI(api_key=API_KEY)
    report = {}

    for day, activity in activities.items():
        prompt = f"Als Fachinformatiker-Azubi habe ich heute folgende Aufgaben erledigt: {activity}. Formuliere diese Stichpunkte in einem vollständigen, professionellen Satz für mein Berichtsheft."

        while True:
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=150,
                    temperature=0.7
                )
                
                generated_text = response.choices[0].message.content.strip()
                report[day] = f"Am {day} : {generated_text}"
                break

            except Exception as e:
                print(f"Ein Fehler ist aufgetreten: {e}")
                report[day] = f"Am {day} konnte der Text nicht generiert werden."
                break
    
    return report