pipeline {
    agent any

    environment {
        GOOGLE_APPLICATION_CREDENTIALS = credentials('gcp-credentials-id')  // Ensure this ID matches the one in Jenkins
    }

    stages {
        stage('Pull Code') {
            steps {
                git 'https://github.com/MehrbanAli065/jenkins.git'
            }
        }
        stage('Build Project') {
            steps {
                sh './build.sh'
            }
        }
        stage('Run Tests') {
            steps {
                sh './test.sh'
            }
        }
        stage('Package Application') {
            steps {
                sh './package.sh'
            }
        }
        stage('Deploy Application') {
            steps {
                withCredentials([file(credentialsId: 'gcp-credentials-id', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    sh 'gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS'
                    sh 'gcloud compute instances create my-instance --zone=us-central1-a --image-family=debian-9 --image-project=debian-cloud'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
