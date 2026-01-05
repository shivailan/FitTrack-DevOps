pipeline {
    agent any
    
    // Bloc de paramètres obligatoires [cite: 64, 66]
    parameters {
        string(name: 'TAILLE', defaultValue: '1.75', description: 'Taille en mètres (ex: 1.75) - Obligatoire') [cite: 29]
        string(name: 'NOM', defaultValue: 'Utilisateur', description: 'Nom de l’utilisateur') [cite: 66]
    }

    stages {
        stage('Installation') {
            steps {
                // Installation sans Docker [cite: 13, 52]
                sh 'python3 -m venv venv' [cite: 60]
                sh './venv/bin/pip install -r requirements.txt' [cite: 60]
            }
        }
        
        stage('Tests') {
            steps {
                // Tests du calcul IMC [cite: 61]
                sh './venv/bin/pytest tests/' [cite: 61]
            }
        }
        
        stage('Génération Rapport PDF') {
            steps {
                // Génération du rapport via script Python [cite: 62]
                sh "./venv/bin/python generate_pdf.py --taille ${params.TAILLE} --nom ${params.NOM}" [cite: 62]
            }
        }
    }
    
    post {
        always {
            // Publication des artefacts PDF [cite: 63]
            archiveArtifacts artifacts: '*.pdf', fingerprint: true [cite: 63]
        }
    }
}