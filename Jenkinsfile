pipeline {
    agent any
    parameters {
        string(name: 'TAILLE', defaultValue: '1.75', description: 'Taille en mètres (ex: 1.75)') [cite: 29, 66]
        string(name: 'NOM', defaultValue: 'Utilisateur', description: 'Nom de l’utilisateur') [cite: 66]
    }
    stages {
        stage('Installation') {
            steps {
                // Création et activation du venv pour isoler les dépendances 
                sh '''
                python3 -m venv venv
                ./venv/bin/pip install --upgrade pip
                ./venv/bin/pip install -r requirements.txt
                '''
            }
        }
        stage('Tests') {
            steps {
                // Utilisation du pytest du venv [cite: 61]
                sh './venv/bin/pytest tests/'
            }
        }
        stage('Génération Rapport PDF') {
            steps {
                // Exécution du script avec les paramètres Jenkins [cite: 62, 66]
                sh "./venv/bin/python generate_pdf.py --taille ${params.TAILLE} --nom ${params.NOM}"
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '*.pdf' [cite: 63]
        }
    }
}