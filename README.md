# Team Setup Guide: Django Docker Projekt

## 1. Einmalige System-Einrichtung

### Software installieren
```bash
# System updaten
sudo apt update
sudo apt upgrade

# Git installieren
sudo apt install git

# Docker installieren
sudo apt install docker.io docker-compose

# VSCode installieren
sudo snap install code --classic
```

### Docker-Berechtigungen einrichten
```bash
# Docker-Gruppe erstellen (falls nicht vorhanden)
sudo groupadd docker

# Deinen Benutzer zur Docker-Gruppe hinzufügen
sudo usermod -aG docker $USER

# Docker Socket Berechtigungen setzen
sudo chmod 666 /var/run/docker.sock

# Docker-Dienst neu starten
sudo systemctl restart docker
```

⚠️ **WICHTIG**: Nach diesen Befehlen MUSST du dich komplett vom System abmelden und wieder anmelden!

### VSCode Extensions installieren
1. VSCode öffnen
2. Diese Extensions installieren:
   - Python
   - Docker
   - Django
   - GitLens

## 2. Projekt klonen und einrichten

### Repository klonen
```bash
# In dein Projekte-Verzeichnis wechseln
cd ~/Projekte  # oder wo auch immer du entwickelst

# Repository klonen
git clone <REPO-URL>
cd django-docker-projekt
```

### Projekt starten
```bash
# Docker Container bauen und starten
docker-compose build
docker-compose up
```

Die Seite sollte jetzt unter http://localhost:8000 erreichbar sein.

## 3. Häufige Entwicklungsbefehle

### Docker-Befehle
```bash
# Server starten
docker-compose up

# Server im Hintergrund starten
docker-compose up -d

# Server stoppen
docker-compose down

# Logs anzeigen (wenn im Hintergrund)
docker-compose logs -f

# Container neu bauen (nach Änderungen an requirements.txt)
docker-compose build --no-cache
```

### Django-Management Befehle
```bash
# Datenbank-Migrationen ausführen
docker-compose run web python manage.py migrate

# Superuser erstellen
docker-compose run web python manage.py createsuperuser

# Django Shell öffnen
docker-compose run web python manage.py shell

# App erstellen
docker-compose run web python manage.py startapp neue_app
```

## 4. Git Workflow

### Täglicher Entwicklungs-Workflow
```bash
# 1. Main-Branch aktualisieren
git checkout main
git pull origin main

# 2. Neuen Feature-Branch erstellen
git checkout -b feature/neue-funktion

# 3. Änderungen vornehmen und committen
git add .
git commit -m "feat: beschreibung der Änderungen"

# 4. Änderungen pushen
git push origin feature/neue-funktion
```

## 5. Troubleshooting

### Problem: Docker-Berechtigungsfehler
```bash
# Überprüfen ob in Docker-Gruppe
groups  # Sollte 'docker' enthalten

# Falls nicht in der Gruppe:
sudo usermod -aG docker $USER
newgrp docker

# Docker neu starten
sudo systemctl restart docker
```

### Problem: Container startet nicht
```bash
# Container stoppen
docker-compose down

# Docker Cache leeren
docker system prune -f

# Neu bauen und starten
docker-compose build --no-cache
docker-compose up
```

### Problem: Migrations-Fehler
```bash
# Alle Migrationen neu ausführen
docker-compose down
rm -rf core/migrations/
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
```

## 6. Best Practices

1. **Vor Arbeitsbeginn**:
   ```bash
   git pull origin main
   docker-compose build
   docker-compose up
   ```

2. **Während der Entwicklung**:
   - Regelmäßig committen
   - Aussagekräftige Commit-Messages schreiben
   - Branch-Namen beschreibend wählen

3. **Code-Qualität**:
   - Tests schreiben
   - PEP8 Standards befolgen
   - Kommentare für komplexe Logik hinzufügen

## 7. Projekt-Struktur
```
django-docker-projekt/
├── config/              # Django Einstellungen
│   ├── settings.py
│   └── urls.py
├── core/               # Haupt-App
│   ├── templates/
│   ├── models.py
│   └── views.py
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

## 8. Hilfe & Support

Bei Problemen:
1. Logs überprüfen: `docker-compose logs`
2. Git-Status prüfen: `git status`
3. Docker-Status prüfen: `docker ps`
4. Team-Mitglieder fragen
5. Issue im Repository erstellen
