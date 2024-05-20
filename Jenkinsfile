pipeline {
    agent any
    
    tools {
        python 'Python 2.7.18' 
    }
    
    stages {
        stage('Build') {
            steps {
                echo 'Application build stage...' 
                sh 'python even.py'
        }
       }
        stage('Test') {
            steps {
                echo 'Application test stage' 
        }
        }
        stage('Run') {
            steps {
                echo 'Application run stage' 
                sh 'python even'
            }
        }
    }
}
