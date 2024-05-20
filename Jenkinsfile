pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Allication build stage...' 
            }
        }
        stage('Test') {
            steps {
                echo 'Allication test stage' 
            }
        }
        stage('Run') {
            steps {
                echo 'Allication run stage'
                
                // Adding a step to print Python code
                sh 'echo "print(\'Hello from Python\')" > hello.py'
                sh 'python hello.py'
            }
        }
    }
}
