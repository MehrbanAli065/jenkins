pipeline {
    agent any
    
    tools {
        jdk 'JDK11' 
    }
    
    stages {
        stage('Build') {
            steps {
                echo 'Application build stage...' 
                sh 'javac prog.java'
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
                sh 'java prog'
            }
        }
    }
}
