import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from .Functions.get_personal_info_and_activities import handle_report_generation

class EasyDailyReport(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title='EasyDailyReport')

        # Titel
        title_label = toga.Label(
            'Ausbildungsnachweis\nWochenberichte einfach erstellen',
            style=Pack(padding=(0, 0, 20, 0), font_size=16, font_weight='bold', alignment='center')
        )

        header_box = toga.Box(
            children=[title_label],
            style=Pack(direction=ROW, alignment='center', padding=10)
        )

        # Personal Information Fields mit fester Breite
        self.name_input = toga.TextInput(style=Pack(width=200, height=30))
        self.ausbildungsberuf_input = toga.TextInput(style=Pack(width=200, height=30))
        self.geschaeftsbereich_input = toga.TextInput(style=Pack(width=200, height=30))
        self.ausbildungsjahr_input = toga.TextInput(style=Pack(width=200, height=30))

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

        # Weekly Activities Fields mit extra Breite
        self.activities = {}
        activities_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
        
        days = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]
        for day in days:
            self.activities[day] = toga.TextInput(style=Pack(width=500, height=60))
            activities_box.add(
                toga.Box(
                    children=[
                        toga.Label(f'{day}:', style=Pack(width=100)),
                        self.activities[day]
                    ],
                    style=Pack(direction=ROW, padding=5)
                )
            )

        # Generate Button
        generate_button = toga.Button(
            'Bericht generieren',
            on_press=self.generate_report,
            style=Pack(padding=5, width=150)
        )

        button_box = toga.Box(
            children=[generate_button],
            style=Pack(direction=ROW, padding=20, alignment='center')
        )

        # Main container
        main_box = toga.Box(
            children=[header_box, personal_box, activities_box, button_box],
            style=Pack(direction=COLUMN, padding=20)
        )

        self.main_window.content = main_box
        self.main_window.show()

    def generate_report(self, widget):
        success = handle_report_generation(self)
        if success:
            self.main_window.info_dialog(
                'Erfolg',
                'Der Bericht wurde erfolgreich erstellt!'
            )

def main():
    return EasyDailyReport('Easy Daily Report', 'org.example.easydailyreport')
