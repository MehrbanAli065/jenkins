pipeline {
    agent any
    
   tools {
        // Install Python
        jenkins.plugins.shiningpanda.tools.PythonInstallation('Python3')
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
