pipeline {
    agent any
    
    // Paramètres obligatoires (Taille demandée au lancement)
    parameters {
        string(name: 'TAILLE', defaultValue: '1.75', description: 'Taille en mètres (ex: 1.75)') [cite: 29, 66]
        string(name: 'NOM', defaultValue: 'Utilisateur', description: 'Nom de l’utilisateur') [cite: 66]
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm [cite: 59]
            }
        }
        
        stage('Installation') {
            steps {
                // Utilisation de venv pour isoler les dépendances sans Docker
                sh 'python3 -m venv venv' [cite: 60]
                sh './venv/bin/pip install -r requirements.txt' [cite: 60]
            }
        }
        
        stage('Tests') {
            steps {
                // Exécution des tests pytest incluant le calcul IMC
                sh './venv/bin/pytest tests/' [cite: 61]
            }
        }
        
        stage('Génération Rapport') {
            steps {
                // On passe la taille du paramètre Jenkins au script Python
                sh "./venv/bin/python generate_pdf.py --taille ${params.TAILLE} --nom ${params.NOM}" [cite: 62]
            }
        }
    }
    
    post {
        always {
            // Publication des artefacts (le PDF généré) et des logs
            archiveArtifacts artifacts: 'reports/*.pdf', fingerprint: true [cite: 63]
        }
    }
}
