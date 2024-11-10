FROM python:3.11-slim

# Setze Arbeitsverzeichnis
WORKDIR /app

# Kopiere requirements und installiere Abhängigkeiten
COPY requirements.txt .
RUN pip install -r requirements.txt

# Kopiere Projektdateien
COPY . .

# Port freigeben
EXPOSE 8000

# Server starten
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
