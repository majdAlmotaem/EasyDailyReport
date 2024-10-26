import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class EasyDailyReport(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title='Easy Daily Report')

        # Personal Information Fields in two columns
        self.name_input = toga.TextInput()
        self.ausbildungsberuf_input = toga.TextInput()
        self.geschaeftsbereich_input = toga.TextInput()
        self.ausbildungsjahr_input = toga.TextInput()

        # Left column
        left_column = toga.Box(
            children=[
                toga.Box(
                    children=[toga.Label('Name:'), self.name_input],
                    style=Pack(direction=ROW, padding=5)
                ),
                toga.Box(
                    children=[toga.Label('Ausbildungsberuf:'), self.ausbildungsberuf_input],
                    style=Pack(direction=ROW, padding=5)
                ),
            ],
            style=Pack(direction=COLUMN, padding=10, flex=1)
        )

        # Right column
        right_column = toga.Box(
            children=[
                toga.Box(
                    children=[toga.Label('Geschäftsbereich:'), self.geschaeftsbereich_input],
                    style=Pack(direction=ROW, padding=5)
                ),
                toga.Box(
                    children=[toga.Label('Ausbildungsjahr:'), self.ausbildungsjahr_input],
                    style=Pack(direction=ROW, padding=5)
                ),
            ],
            style=Pack(direction=COLUMN, padding=10, flex=1)
        )

        # Personal box with two columns
        personal_box = toga.Box(
            children=[left_column, right_column],
            style=Pack(direction=ROW, padding=10)
        )

        # Weekly Activities Fields
        self.activities = {}
        activities_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        
        days = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]
        for day in days:
            self.activities[day] = toga.TextInput()
            activities_box.add(
                toga.Box(
                    children=[
                        toga.Label(f'{day}:'),
                        self.activities[day]
                    ],
                    style=Pack(direction=ROW, padding=5)
                )
            )

        # Main container
        main_box = toga.Box(
            children=[personal_box, activities_box],
            style=Pack(direction=COLUMN, padding=20)
        )

        self.main_window.content = main_box
        self.main_window.show()

def main():
    return EasyDailyReport('Easy Daily Report', 'org.example.easydailyreport')
