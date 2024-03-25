pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/tharaas/TrelloProject'
            }
        }
        stage('Read .env file') {
            steps {
                // Read .env file and set environment variables
                withCredentials([file(credentialsId: 'jenkins-env-file', variable: 'ENV_FILE')]) {
                    bat 'type %ENV_FILE%'
                    script {
                        def envFileContent = readFile(env.ENV_FILE).trim()
                        envFileContent.eachLine { line ->
                            def (key, value) = line.tokenize('=')
                            env."${key.trim()}" = value.trim()
                        }
                    }
                }
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'cd'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh 'python test_runner.py'
            }
        }
    }

    post {
        success {
            echo 'Tests passed successfully!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}