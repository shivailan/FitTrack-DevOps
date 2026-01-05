pipeline {
    agent any
    parameters {
        // Taille via Jenkins Parameters (Obligatoire) [cite: 29, 66]
        string(name: 'TAILLE', defaultValue: '1.75', description: 'Taille en m')
        string(name: 'NOM', defaultValue: 'Shiva', description: 'Nom utilisateur')
    }
    stages {
        stage('Installation') {
            steps { sh 'python3 -m pip install -r requirements.txt' } // 
        }
        stage('Tests') {
            steps { sh 'export PYTHONPATH=. && python3 -m pytest tests/' } // 
        }
        stage('Rapport PDF') {
            steps { 
                // Génération automatique du rapport [cite: 62]
                sh "python3 generate_pdf.py --taille ${params.TAILLE} --nom ${params.NOM}" 
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: '*.pdf' // Publication des artefacts [cite: 63]
        }
    }
}