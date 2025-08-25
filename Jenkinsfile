pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/Indra9894/e-commerce.git'
        DOCKER_COMPOSE_FILE = 'docker-compose.yml'
        BACKEND_IMAGE = 'ecommerce-backend:latest'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: "${env.REPO_URL}"
            }
        }

        stage('Build Backend Docker Image') {
            steps {
                dir('backend') {
                    sh 'docker build -t $BACKEND_IMAGE .'
                }
            }
        }

        stage('Run Docker Compose') {
            steps {
                sh "docker-compose -f ${env.DOCKER_COMPOSE_FILE} down"
                sh "docker-compose -f ${env.DOCKER_COMPOSE_FILE} up -d --build"
            }
        }

        stage('Clean Up') {
            steps {
                sh "docker system prune -f"
            }
        }
    }

    post {
        success {
            echo 'Deployment Successful!'
        }
        failure {
            echo 'Deployment Failed!'
        }
    }
}
