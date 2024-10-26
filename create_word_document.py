import os

from docx import Document
from get_week_dates import get_week_dates
from create_reports_directory import create_reports_directory

def create_word_document(report):
    # Get the reports directory
    reports_folder = create_reports_directory()
    
    # Erstelle ein neues Word-Dokument
    doc = Document()
    
    # Überschrift und Datum
    doc.add_heading('Ausbildungsnachweis', 0)
    start_date, end_date = get_week_dates()
    doc.add_paragraph(f'Ausbildungswoche vom: {start_date} bis: {end_date}\n')
    
    # Füge für jeden Tag die Aktivitäten hinzu
    for day, text in report.items():
        doc.add_heading(day, level=2)
        doc.add_paragraph(text)
    
    # Speichern im Berichtshefte-Ordner
    filename = f'Ausbildungsnachweis_{start_date}_bis_{end_date}.docx'
    filepath = os.path.join(reports_folder, filename)
    doc.save(filepath)
    
    print(f'Dokument erfolgreich erstellt: {filepath}')
