pipeline {
    agent any

    environment {
        // Define environment variables if necessary
        GCP_CREDENTIALS = credentials('my-key') // Assuming you have added the GCP service account key in Jenkins credentials
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/MehrbanAli065/jenkins.git' // Replace with your repository URL
            }
        }

        stage('Build') {
            steps {
                echo 'Building...' // Replace with your build command or script
            }
        }

        stage('Test') {
            steps {
                sh './run_tests.sh' // Replace with your test command or script
            }
        }

        stage('Package') {
            steps {
                echo 'Packaging...' // Replace with your package command or script
            }
        }

        stage('Deploy') {
            steps {
                script {
                    withCredentials([file(credentialsId: 'my-key', variable: 'GCP_KEY_FILE')]) {
                        sh """
                            gcloud auth activate-service-account --key-file=$GCP_KEY_FILE
                            gcloud config set project genuine-habitat-423301-a2
                            gcloud compute instances create example-instance \
                                --image-family=debian-9 --image-project=debian-cloud
                        """ // Replace with your GCP deployment commands
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs() // Clean workspace after build
        }
    }
}
