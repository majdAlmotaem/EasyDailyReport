from get_weekly_activities import get_weekly_activities
from generate_report_text import generate_report_text
from create_word_document import create_word_document
from get_personal_informations import get_personal_informations

def main():
    # Get personal informations first
    personal_informations = get_personal_informations()
    
    # Get activities and generate report
    activities = get_weekly_activities()
    report = generate_report_text(activities)
    
    # Create document with both personal info and report
    create_word_document(report, personal_informations)

if __name__ == "__main__":
    main()