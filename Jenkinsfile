pipeline {
    agent {
        node {
            label ''
            // Esto le da permisos de administrador (root) al pipeline
            customWorkspace "/var/jenkins_home/workspace/${env.JOB_NAME}"
        }
    }

    stages {
        stage('Checkout (Ingredientes)') {
            steps {
                echo 'Descargando el código desde GitHub...'
                checkout scm
            }
        }

        stage('Test (Control de Calidad)') {
            steps {
                echo 'Instalando entorno y ejecutando PyBuilder...'
                // Instalamos pip y pybuilder usando el usuario root
                sh '''
                    apt-get update
                    apt-get install -y python3-pip
                    python3 -m pip install --upgrade pip
                    python3 -m pip install pybuilder
                    python3 -m pyb
                '''
            }
        }

        stage('Build (Cocinar)') {
            steps {
                echo 'Construyendo la imagen de Docker...'
                sh 'docker build -t bioguard-app .'
            }
        }

        stage('Deploy (Servir)') {
            steps {
                echo 'Desplegando en puerto seguro 8443...'
                sh 'docker stop bioguard-container || true'
                sh 'docker rm bioguard-container || true'
                sh 'docker run -d -p 8443:5000 --name bioguard-container bioguard-app'
            }
        }
    }

    post {
        success {
            echo '¡Auditoría superada! Vacunas seguras en puerto 8443.'
        }
        failure {
            echo '¡BLOQUEO DE SEGURIDAD! Revisa los permisos o el código.'
        }
    }
}
