pipeline {
    agent any

    // Paramètres obligatoires demandés au lancement du build 
    parameters {
        string(name: 'TAILLE', defaultValue: '1.75', description: 'Taille en mètres (ex: 1.75) - Obligatoire pour le calcul IMC')
        string(name: 'NOM', defaultValue: 'Utilisateur', description: 'Nom de l’utilisateur pour le rapport PDF')
    }

    stages {
        stage('Checkout') {
            steps {
                // Récupération du code depuis GitHub [cite: 59]
                checkout scm
            }
        }

        stage('Installation') {
            steps {
                // Création de l'environnement virtuel et installation des dépendances [cite: 60]
                sh '''
                python3 -m venv venv
                ./venv/bin/pip install --upgrade pip
                ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Tests') {
            steps {
                // Exécution des tests unitaires avec export du chemin pour trouver app.py [cite: 61]
                sh '''
                export PYTHONPATH=.
                ./venv/bin/pytest tests/
                '''
            }
        }

        stage('Génération Rapport PDF') {
            steps {
                // Script Python générant le rapport PDF avec les paramètres Jenkins [cite: 62]
                sh "./venv/bin/python generate_pdf.py --taille ${params.TAILLE} --nom ${params.NOM}"
            }
        }
    }

    post {
        always {
            // Publication des artefacts (PDF) et des logs d'exécution [cite: 63]
            archiveArtifacts artifacts: '*.pdf', fingerprint: true
        }
    }
}