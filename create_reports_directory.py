import os

def create_reports_directory():
    """Creates a directory named 'Berichtshefte' if it doesn't exist"""
    reports_folder = "Berichtshefte"
    os.makedirs(reports_folder, exist_ok=True)
    return reports_folder
