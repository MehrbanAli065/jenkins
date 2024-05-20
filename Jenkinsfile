pipeline {
    agent any
    
   tools {
        // Install Python
        python 'Python 3.9.6'
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
                
            }
        }
    }
}
