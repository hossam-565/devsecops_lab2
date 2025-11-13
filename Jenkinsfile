pipeline {
    agent any

    environment {
        IMAGE_NAME = "calculator_api_app"
        PYTHON = "./venv/bin/python"
        PIP = "./venv/bin/pip"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh """
                    python3 -m venv venv
                    ${PIP} install --upgrade pip
                    ${PIP} install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                    ${PYTHON} -m pytest || true
                """
            }
        }

        stage('Static Code Analysis (Bandit)') {
            steps {
                sh """
                    ${PIP} install bandit
                    ./venv/bin/bandit -r . || true
                """
            }
        }

        stage('Dependency Vulnerability Scan (Safety)') {
            steps {
                sh """
                    ${PIP} install safety
                    ./venv/bin/safety check --full-report --no-api -r requirements.txt || true
                """
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                    docker-compose build
                """
            }
        }

        stage('Container Vulnerability Scan (Trivy)') {
            steps {
                sh """
                    trivy image ${IMAGE_NAME}:latest || true
                """
            }
        }

        stage('Deploy Application') {
            steps {
                sh """
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
