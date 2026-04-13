pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test (Control de Calidad)') {
            steps {
                echo 'Instalando herramientas de Python...'
                sh '''
                    apt-get update
                    apt-get install -y python3-pip
                    python3 -m pip install --upgrade pip --break-system-packages
                    python3 -m pip install pybuilder --break-system-packages
                    python3 -m pyb
                '''
            }
        }

        stage('Build & Deploy') {
            steps {
                sh 'docker build -t bioguard-app .'
                sh 'docker stop bioguard-container || true'
                sh 'docker rm bioguard-container || true'
                sh 'docker run -d -p 8443:5000 --name bioguard-container bioguard-app'
            }
        }
    }
    
    post {
        success { echo '¡TODO EN VERDE! BioGuard desplegado en puerto 8443.' }
        failure { echo 'Fallo en el pipeline.' }
    }
}
