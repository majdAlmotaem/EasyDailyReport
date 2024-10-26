from datetime import datetime, timedelta

def get_week_dates():
    """Returns the Monday and Friday dates of the current week"""
    today = datetime.now()
    monday = today - timedelta(days=today.weekday())  # Go back to Monday
    friday = monday + timedelta(days=4)  # Add 4 days to get to Friday
    
    return monday.strftime("%d.%m.%Y"), friday.strftime("%d.%m.%Y")