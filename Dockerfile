# Utiliser une image officielle de Python
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Spécifier le port (Render lit automatiquement la variable d’environnement PORT)
ENV PORT=5000

# Lancer l'application
CMD ["python", "app.py"]
