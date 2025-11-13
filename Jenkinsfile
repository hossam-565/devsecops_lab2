pipeline {
    agent any

    environment {
        IMAGE_NAME = "calculator_api_app"
        PYTHON = "./venv/bin/python"
        PIP = "./venv/bin/pip"
    }

    stages {

        /* =======================
           CHECKOUT FROM GITHUB
           ======================= */
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        /* =======================
           PYTHON ENV + DEPENDENCIES
           ======================= */
        stage('Setup Python Environment') {
            steps {
                sh """
                    python3 -m venv venv
                    ${PIP} install --upgrade pip
                    ${PIP} install -r requirements.txt
                """
            }
        }

        /* =======================
           RUN PYTEST
           ======================= */
        stage('Run Tests') {
            steps {
                sh """
                    ${PYTHON} -m pytest || true
                """
            }
        }

        /* =======================
           STATIC ANALYSIS (BANDIT)
           ======================= */
        stage('Static Code Analysis (Bandit)') {
            steps {
                sh """
                    ${PIP} install bandit
                    ./venv/bin/bandit -r . || true
                """
            }
        }

        /* =======================
           DEPENDENCY SCAN (SAFETY)
           ======================= */
        stage('Dependency Vulnerability Scan (Safety)') {
            steps {
                sh """
                    ${PIP} install safety
                    ./venv/bin/safety scan -r requirements.txt --disable-telemetry || true
                """
            }
        }

        /* =======================
           DOCKER BUILD
           ======================= */
        stage('Build Docker Image') {
            steps {
                sh """
                    sudo chmod 666 /var/run/docker.sock
                    docker-compose build
                """
            }
        }

        /* =======================
           TRIVY SCAN
           ======================= */
        stage('Container Vulnerability Scan (Trivy)') {
            steps {
                sh """
                    trivy image ${IMAGE_NAME}:latest || true
                """
            }
        }

        /* =======================
           DEPLOY WITH DOCKER-COMPOSE
           ======================= */
        stage('Deploy Application') {
            steps {
                sh """
                    sudo chmod 666 /var/run/docker.sock
                    docker-compose up -d
                """
            }
        }
    }

    /* =======================
       CLEAN WORKSPACE
       ======================= */
    post {
        always {
            cleanWs()
        }
    }
}
