def get_personal_info(app):
    """Sammelt die persönlichen Informationen aus den Eingabefeldern"""
    return (
        app.name_input.value,
        app.ausbildungsberuf_input.value,
        app.geschaeftsbereich_input.value,
        app.ausbildungsjahr_input.value
    )

def get_activities(app):
    """Sammelt die Aktivitäten aus den Tages-Eingabefeldern"""
    return {day: input.value for day, input in app.activities.items()}

def handle_report_generation(app):
    """Hauptfunktion zur Berichterstellung"""
    from .generate_report_text import generate_report_text
    from .create_word_document import create_word_document
    
    personal_info = get_personal_info(app)
    activities = get_activities(app)
    report = generate_report_text(activities)
    create_word_document(report, personal_info)
    return True
