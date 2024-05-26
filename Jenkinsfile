pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/MehrbanAli065/jenkins.git' // Replace with your repository URL
            }
        }

        stage('Deploy to Google Cloud') {
            steps {
                script {
                    try {
                        withCredentials([file(credentialsId: 'key', variable: 'GCP_KEY_FILE')]) {
                            sh 'gcloud auth activate-service-account --key-file=$GCP_KEY_FILE'
                            sh 'gcloud config set project genuine-habitat-423301-a2' // Replace with your GCP project ID
                            sh 'gcloud compute scp index.html ar784419@mjenkins:/var/www/html' // Replace with your GCP instance SSH username, instance name, and destination path
                            echo 'Successfully deployed index.html to Google Cloud server'
                        }
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        error("Failed to deploy index.html to Google Cloud server: ${e.message}")
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Successfully deployed!'
        }
    }
}
