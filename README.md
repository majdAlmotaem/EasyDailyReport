# EasyDailyReport 📝
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Eine automatisierte Lösung zur Erstellung von Ausbildungsnachweisen mit KI-Unterstützung.

## 🎯 Funktionen

- **Automatische Textgenerierung**: Verwendet Google Gemini AI, um professionelle Beschreibungen Ihrer täglichen Aktivitäten zu erstellen
- **Word-Dokument Erstellung**: Generiert automatisch formatierte Word-Dokumente im Standard-Ausbildungsnachweis Format
- **Benutzerfreundliche Eingabe**: Einfache Eingabe der täglichen Aktivitäten über die Kommandozeile
- **Professionelles Format**: Standardisiertes Layout mit Kopfzeile, Aktivitätentabelle und Unterschriftenbereichen

## 🚀 Installation

1. Klonen Sie das Repository:
```bash
git clone https://github.com/YourUsername/EasyDailyReport.git
cd EasyDailyReport
```

2. Installieren Sie die erforderlichen Abhängigkeiten:
```bash
pip install -r requirement.txt
```

3. Erstellen Sie eine `config.py` Datei mit Ihrem Google Gemini API-Key:
```python
API_KEY = 'Ihr-Google-Gemini-API-Key'
```

## 💻 Verwendung

1. Starten Sie das Programm:
```bash
python main.py
```

2. Folgen Sie den Eingabeaufforderungen:
   - Geben Sie Ihre persönlichen Informationen ein (Name, Ausbildungsberuf, etc.)
   - Beschreiben Sie Ihre täglichen Aktivitäten für jeden Arbeitstag

3. Das Programm wird automatisch:
   - Ihre Aktivitätsbeschreibungen in professionelle Sätze umwandeln
   - Ein formatiertes Word-Dokument erstellen
   - Das Dokument im reports-Ordner speichern

## 📋 Anforderungen

- Python 3.8 oder höher
- Google Gemini API-Key
- Installierte Abhängigkeiten (siehe requirement.txt):
  - google-generativeai>=0.8.3
  - python-docx>=1.1.2
  - lxml>=5.3.0

## 🔧 Konfiguration

Die Anwendung verwendet folgende Konfigurationsdateien:
- `config.py`: Enthält den API-Key für Google Gemini
- `requirement.txt`: Liste der Python-Abhängigkeiten

## 📁 Projektstruktur

- `main.py`: Hauptprogramm und Einstiegspunkt
- `generate_report_text.py`: KI-gestützte Textgenerierung
- `create_word_document.py`: Word-Dokument Erstellung und Formatierung
- `get_weekly_activities.py`: Erfassung der täglichen Aktivitäten
- `get_personal_informations.py`: Erfassung der persönlichen Informationen

## 🤝 Beitrag

Verbesserungsvorschläge sind willkommen! Öffnen Sie einfach ein Issue oder erstellen Sie einen Pull Request.

## 📝 Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die [LICENSE](LICENSE) Datei für Details.

## ⚠️ Hinweis

Stellen Sie sicher, dass Sie Ihren Google Gemini API-Key sicher aufbewahren und nicht im Repository veröffentlichen.
