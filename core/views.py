# core/views.py
from django.views.generic import TemplateView
from .models import Item

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Item.objects.all()
        return context

class SetupGuideView(TemplateView):
    template_name = 'core/django-setup-guide.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Code-Beispiele als Kontext-Variablen
        context['software_installation'] = """# System updaten
sudo apt update
sudo apt upgrade

# Git installieren
sudo apt install git

# Docker installieren
sudo apt install docker.io docker-compose

# VSCode installieren
sudo snap install code --classic"""

        context['docker_permissions'] = """# Docker-Gruppe erstellen (falls nicht vorhanden)
sudo groupadd docker

# Deinen Benutzer zur Docker-Gruppe hinzufügen
sudo usermod -aG docker $USER

# Docker Socket Berechtigungen setzen
sudo chmod 666 /var/run/docker.sock

# Docker-Dienst neu starten
sudo systemctl restart docker"""

        context['git_clone'] = """# In dein Projekte-Verzeichnis wechseln
cd ~/Projekte  # oder wo auch immer du entwickelst

# Repository klonen
git clone <REPO-URL>
cd django-docker-projekt"""

        context['project_start'] = """# Docker Container bauen und starten
docker-compose build
docker-compose up"""

        context['docker_commands'] = """# Server starten
docker-compose up

# Server im Hintergrund starten
docker-compose up -d

# Server stoppen
docker-compose down

# Logs anzeigen (wenn im Hintergrund)
docker-compose logs -f

# Container neu bauen (nach Änderungen an requirements.txt)
docker-compose build --no-cache"""

        context['django_commands'] = """# Datenbank-Migrationen ausführen
docker-compose run web python manage.py migrate

# Superuser erstellen
docker-compose run web python manage.py createsuperuser

# Django Shell öffnen
docker-compose run web python manage.py shell

# App erstellen
docker-compose run web python manage.py startapp neue_app"""

        context['git_workflow'] = """# 1. Main-Branch aktualisieren
git checkout main
git pull origin main

# 2. Neuen Feature-Branch erstellen
git checkout -b feature/neue-funktion

# 3. Änderungen vornehmen und committen
git add .
git commit -m "feat: beschreibung der Änderungen"

# 4. Änderungen pushen
git push origin feature/neue-funktion"""

        context['docker_troubleshooting'] = """# Überprüfen ob in Docker-Gruppe
groups  # Sollte 'docker' enthalten

# Falls nicht in der Gruppe:
sudo usermod -aG docker $USER
newgrp docker

# Docker neu starten
sudo systemctl restart docker"""

        context['container_troubleshooting'] = """# Container stoppen
docker-compose down

# Docker Cache leeren
docker system prune -f

# Neu bauen und starten
docker-compose build --no-cache
docker-compose up"""

        context['migration_troubleshooting'] = """# Alle Migrationen neu ausführen
docker-compose down
rm -rf core/migrations/
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate"""

        context['before_work'] = """git pull origin main
docker-compose build
docker-compose up"""

        context['project_structure'] = """django-docker-projekt/
├── config/              # Django Einstellungen
│   ├── settings.py
│   └── urls.py
├── core/               # Haupt-App
│   ├── templates/
│   ├── models.py
│   └── views.py
├── docker-compose.yml
├── Dockerfile
└── requirements.txt"""

        return context