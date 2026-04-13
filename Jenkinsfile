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
                echo 'Ejecutando pruebas de calidad...'
                // Aquí cambiaremos el comando en el siguiente paso
                sh 'python test.py'
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
                echo 'Desplegando la aplicación...'
                // Aquí cambiaremos el puerto en el siguiente paso
                sh 'docker run -d -p 5000:5000 --name bioguard-container bioguard-app'
            }
        }
    }

    post {
        success {
            echo '¡La hamburguesa... digo, la vacuna, está lista y segura!'
        }
        failure {
            echo '¡Error en la fábrica! Revisa los logs.'
        }
    }
}
