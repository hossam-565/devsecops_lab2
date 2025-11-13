pipeline {
    agent any

    environment {
        IMAGE_NAME = 'calculator-api-app'
    }

    stages {

        stage('Checkout') {
            steps {
                // Récupère le code depuis ton repo GitHub
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh """
                    python3 -m venv venv
                    ./venv/bin/pip install --upgrade pip
                    ./venv/bin/pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                    ./venv/bin/pytest || true
                """
            }
        }

        stage('Static Code Analysis (Bandit)') {
            steps {
                sh """
                    ./venv/bin/pip install bandit
                    ./venv/bin/bandit -r . || true
                """
            }
        }

        stage('Dependency Vulnerability Scan (Safety)') {
            steps {
                sh """
                    ./venv/bin/pip install safety
                    # IMPORTANT : mode non interactif, pas de login
                    ./venv/bin/safety check --full-report --no-api -r requirements.txt || true
                """
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                    # PAS de sudo ici, les droits Docker doivent être déjà réglés sur la machine
                    docker-compose build
                """
            }
        }

        stage('Container Vulnerability Scan (Trivy)') {
            steps {
                sh """
                    # Scan de l'image Docker avec Trivy
                    trivy image ${IMAGE_NAME}:latest || true
                """
            }
        }

        stage('Deploy Application') {
            steps {
                sh """
                    docker rm -f calculator-api || true
                    docker-compose down --remove-orphans || true
                    docker-compose up -d
                """
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
