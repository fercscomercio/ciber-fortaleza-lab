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
                echo 'Instalando herramientas y ejecutando auditoría...'
                // 1. Actualiza pip e instala pybuilder dentro de Jenkins
                sh 'pip install --upgrade pip'
                sh 'pip install pybuilder'
                
                // 2. Ejecuta el comando usando 'python3 -m pyb' 
                // para asegurar que encuentra el ejecutable recién instalado
                sh 'python3 -m pyb' 
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
                // Limpieza de contenedores previos para evitar conflictos
                sh 'docker stop bioguard-container || true'
                sh 'docker rm bioguard-container || true'
                
                // MODIFICACIÓN: Despliegue en puerto seguro 8443
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
