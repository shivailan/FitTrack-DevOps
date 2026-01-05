pipeline {
    agent any
    parameters {
        string(name: 'TAILLE', defaultValue: '1.75', description: 'Taille en mètres [cite: 29]')
        string(name: 'NOM', defaultValue: 'Utilisateur', description: 'Nom [cite: 66]')
    }
    stages {
        stage('Installation') {
            steps {
                // On utilise python3 -m pip pour éviter l'erreur "command not found" [cite: 60]
                sh 'python3 -m pip install --user -r requirements.txt'
            }
        }
        stage('Tests') {
            steps {
                // Exécution de pytest pour valider le calcul IMC [cite: 35, 61]
                sh 'python3 -m pytest tests/'
            }
        }
        stage('Génération Rapport PDF') {
            steps {
                // Script de génération du rapport final [cite: 42, 62]
                sh "python3 generate_pdf.py --taille ${params.TAILLE} --nom ${params.NOM}"
            }
        }
    }
    post {
        always {
            // Publication des artefacts PDF obligatoires [cite: 63, 78]
            archiveArtifacts artifacts: '*.pdf', fingerprint: true
        }
    }
}
