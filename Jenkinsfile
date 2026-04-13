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
                echo 'Instalando PyBuilder y ejecutando auditoría...'
                sh '''
                    # 1. Aseguramos que pip esté presente sin intentar actualizarlo
                    apt-get update
                    apt-get install -y python3-pip
                    
                    # 2. Instalamos PyBuilder y Flask (usando la bandera para saltar el bloqueo)
                    python3 -m pip install pybuilder flask --break-system-packages
                    
                    # 3. Ejecutamos la auditoría
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
