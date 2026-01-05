pipeline {
    agent any
    
    parameters {
        // La taille est obligatoire via Jenkins Parameters 
        string(name: 'TAILLE', defaultValue: '1.75', description: 'Taille en mètres (ex: 1.75)')
        string(name: 'NOM', defaultValue: 'Utilisateur', description: 'Nom de l’utilisateur')
    }

    stages {
        stage('Installation') {
            steps {
                // Installation des dépendances sans Docker [cite: 13, 52, 60]
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Tests') {
            steps {
                // Exécution des tests pytest incluant le calcul IMC [cite: 61]
                sh 'pytest tests/'
            }
        }
        
        stage('Génération Rapport PDF') {
            steps {
                // Génération automatique du rapport PDF [cite: 62]
                sh "python generate_pdf.py --taille ${params.TAILLE} --nom ${params.NOM}"
            }
        }
    }
    
    post {
        always {
            // Publication des résultats et des artefacts PDF [cite: 63]
            archiveArtifacts artifacts: '*.pdf', fingerprint: true
        }
    }
}
