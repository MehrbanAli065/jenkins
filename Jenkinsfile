pipeline {
    agent any

    environment {
        GOOGLE_APPLICATION_CREDENTIALS = credentials('my-key')
    }

    stages {
        stage('Authenticate') {
            steps {
                sh 'gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS'
            }
        }

        stage('List Instances') {
            steps {
                sh 'gcloud compute instances list'
            }
        }
    }
}
