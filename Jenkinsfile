pipeline {
    agent any
    options {
        timestamps()
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timeout(time: 15, unit: 'MINUTES')
    }
    triggers {
        pollSCM('* * * * *')
    }
    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt -r requirements-dev.txt
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                . venv/bin/activate
                pytest --junitxml=report.xml
                '''
            }
            post {
                always {
                    junit 'report.xml'
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                sh "docker build -t lakshpacholy/flask-app:${env.BUILD_NUMBER} -t lakshpacholy/flask-app:latest ."
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                docker stop flask-app || true
                docker rm flask-app || true
                docker run -d -p 8000:8000 --name flask-app lakshpacholy/flask-app:latest
                sleep 5
                curl -f http://localhost:8000/health
                '''
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
        always {
            sh 'docker image prune -f'
        }
    }
}
