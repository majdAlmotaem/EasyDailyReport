def get_weekly_activities():
    days = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]
    activities = {}
    
    for day in days:
        activities[day] = input(f"Was hast du am {day} gemacht? ")
    
    return activities
