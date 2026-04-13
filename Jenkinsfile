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
                    # 1. Aseguramos pip (ya lo tienes, pero por seguridad)
                    apt-get update && apt-get install -y python3-pip
                    
                    # 2. Instalamos PyBuilder
                    python3 -m pip install pybuilder flask --break-system-packages
                    
                    # 3. EJECUCIÓN DIRECTA (Aquí está el truco)
                    # Usamos 'python3 -m pybuilder' en lugar de solo 'pybuilder'
                    python3 -m pybuilder -v
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
