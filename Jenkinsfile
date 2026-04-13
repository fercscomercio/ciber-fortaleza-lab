pipeline {
    agent any

    stages {
        stage('Checkout (Ingredientes)') {
            steps {
                echo 'Descargando el código desde GitHub...'
                checkout scm
            }
        }

        stage('Test (Control de Calidad)') {
            steps {
                echo 'Ejecutando auditoría con PyBuilder...'
                // MODIFICACIÓN 1: Usamos pyb para validar cobertura y PEP8
                sh 'pyb' 
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
                echo 'Desplegando en puerto seguro...'
                sh 'docker stop bioguard-container || true'
                sh 'docker rm bioguard-container || true'
                // MODIFICACIÓN 2: Cambiamos el puerto de escucha al 8443
                sh 'docker run -d -p 8443:5000 --name bioguard-container bioguard-app'
            }
        }
    }

    post {
        success {
            echo '¡Auditoría superada! Vacunas seguras en puerto 8443.'
        }
        failure {
            echo '¡BLOQUEO DE SEGURIDAD! El código no cumple los estándares.'
        }
    }
}
