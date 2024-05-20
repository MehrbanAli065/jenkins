pipeline {
    agent any
    
   environment {
        // Define the installation directory for Python
        PYTHON_HOME = tool name: 'Python 3.9.6', type: 'hudson.plugins.python.PythonInstallation', label: ''
    }
    
    stages {
        stage('Build') {
            steps {
                echo 'Application build stage...' 
                sh "${PYTHON_HOME}/bin/python even.py"
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
