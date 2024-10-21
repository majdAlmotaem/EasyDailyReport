from docx import Document
from datetime import datetime

def create_word_document(report):
    # Erstelle ein neues Word-Dokument
    doc = Document()
    
    # Überschrift und Datum
    doc.add_heading('Ausbildungsnachweis', 0)
    start_date = datetime.now().strftime("%d.%m.%Y")
    end_date = datetime.now().strftime("%d.%m.%Y")  # Zum Beispiel
    doc.add_paragraph(f'Ausbildungswoche vom: {start_date} bis: {end_date}\n')
    
    # Füge für jeden Tag die Aktivitäten hinzu
    for day, text in report.items():
        doc.add_heading(day, level=2)
        doc.add_paragraph(text)
    
    # Speichern
    filename = f'Ausbildungsnachweis_{start_date}_bis_{end_date}.docx'
    doc.save(filename)
    
    print(f'Dokument erfolgreich erstellt: {filename}')
