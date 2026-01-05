pipeline {
    agent any
    
    parameters {
        // La taille est obligatoire via Jenkins Parameters pour le calcul IMC [cite: 29, 35]
        string(name: 'TAILLE', defaultValue: '1.75', description: 'Taille en mètres (ex: 1.75) - Obligatoire')
        string(name: 'NOM', defaultValue: 'Utilisateur', description: 'Nom de l’utilisateur')
    }

    stages {
        stage('Installation') {
            steps {
                // Utilisation d'un venv pour éviter les erreurs de permissions [cite: 60]
                sh '''
                python3 -m venv venv
                ./venv/bin/pip install --upgrade pip
                ./venv/bin/pip install -r requirements.txt
                '''
            }
        }
        
        stage('Tests') {
            steps {
                // Tests du calcul IMC obligatoire [cite: 35, 61]
                sh './venv/bin/pytest tests/'
            }
        }
        
        stage('Génération Rapport PDF') {
            steps {
                // Génération du rapport PDF incluant le journal Mars-Mai [cite: 40, 62]
                sh "./venv/bin/python generate_pdf.py --taille ${params.TAILLE} --nom ${params.NOM}"
            }
        }
    }
    
    post {
        always {
            // Publication des artefacts PDF (Exigence 6.1.5) [cite: 63]
            archiveArtifacts artifacts: '*.pdf', fingerprint: true
        }
    }
}