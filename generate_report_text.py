from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_report_text(activities):
    report = {}
    
    for day, activity in activities.items():
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Du bist ein hilfreicher Assistent, der Stichpunkte in vollständige Sätze umwandelt."},
                {"role": "user", "content": f"Formuliere diesen Stichpunkt in einen vollständigen Satz: {activity}"}
            ]
        )
        
        generated_text = response.choices[0].message.content.strip()
        report[day] = f"Am {day} habe ich {generated_text}"
    
    return report