from get_weekly_activities import get_weekly_activities
from generate_report_text import generate_report_text
from create_word_document import create_word_document

def main():
    activities = get_weekly_activities()
    report = generate_report_text(activities)
    create_word_document(report)

if __name__ == "__main__":
    main()
