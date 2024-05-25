pipeline {
    agent any

    environment {
        GCP_CREDENTIALS = credentials('gcp-credentials-id')
        
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
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-credentials-id']]) {
                    sh 'aws deploy create-deployment --application-name my-app --deployment-group-name my-deployment-group --s3-location bucket=my-bucket,bundleType=zip,key=my-key'
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
