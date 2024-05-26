pipeline {
    agent any 
    environment {
        GOOGLE_CREDENTIALS = credentials('my-key') // Ensure 'your-credential-id' is the correct ID for your credentials
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                script {
                    withCredentials([file(credentialsId: 'my-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                        // Your build steps here, e.g., running a script
                        sh 'gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS'
                        // other GCP related commands
                    }
                }
            }
        }
    }
    post {
        always {
            echo 'Pipeline completed!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
