pipeline {
    agent any
    
   environment {
        PYTHON_HOME = tool name: 'Python3', type: 'jenkins.plugins.shiningpanda.tools.PythonInstallation'
        PATH = "${env.PYTHON_HOME}/bin:${env.PATH}"
    }
    
    stages {
        stage('Build') {
            steps {
                echo 'Application build stage...' 
                sh 'python --version'
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
                echo "This is my IP"
                curl -s ifconfig.co
                echo "This is my hostname"
                hostname -f
                
            }
        }
    }
}
