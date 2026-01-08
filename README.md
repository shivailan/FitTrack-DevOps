🥗 FitTrack DevOps - Suivi Minceur
Projet de validation CI/CD et Agilité

Lien JIRA : https://shivailan.atlassian.net/jira/software/projects/FV/boards/3?atlOrigin=eyJpIjoiZmQ3MGI0M2IyODNmNDBiYzg1ZmNmYmYyYThiZjRiZTMiLCJwIjoiaiJ9

Ce projet est une application MVP (Minimum Viable Product) de suivi de santé permettant de calculer l'IMC, d'enregistrer le poids et les repas, et de générer des rapports automatisés.

🚀 Fonctionnalités
Interface Flask : Formulaire de saisie pour le poids, la taille et les repas.

Logique métier : Calcul automatique de l'IMC et classification (Normal, Surpoids, etc.).

Persistance : Stockage sur base de données PostgreSQL.

Pipeline CI/CD : Automatisation complète sous Jenkins (Tests unitaires + Génération de rapport PDF).

🛠 Installation et Lancement
1. Base de données

Assurez-vous que PostgreSQL est démarré, puis exécutez le script d'initialisation :

Bash
createdb fittrack
psql -d fittrack -f database.sql
Note : Le script contient déjà les données de démo pour la période obligatoire de Mars à Mai.

2. Application Flask

Bash
# Installation des dépendances
pip install -r requirements.txt

# Lancement de l'interface
python app.py
Accédez à l'interface sur : http://127.0.0.1:5000

3. Pipeline Jenkins

Le fichier Jenkinsfile à la racine permet de configurer le build.

Paramètres requis : NOM (String) et TAILLE (String, ex: 1.75).

Artefact : Le rapport Rapport_Final_FitTrack.pdf est généré à la fin de chaque build réussi.

📈 Organisation Agile
Le suivi du projet a été réalisé via un Board GitHub Projects (To Do / In Progress / Done) et la gestion des anomalies via les GitHub Issues.
