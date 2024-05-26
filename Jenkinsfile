pipeline {
    agent any

    environment {
        GOOGLE_APPLICATION_CREDENTIALS = credentials('my-key')
    }

    stages {
        stage('Authenticate') {
            steps {
                script {
                    withCredentials([file(credentialsId: 'my-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                        sh 'echo $GOOGLE_APPLICATION_CREDENTIALS'
                        sh 'gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS'
                    }
                }
            }
        }

        stage('List Instances') {
            steps {
                sh 'gcloud compute instances list'
                echo 'success'
            }
        }
    }
}
