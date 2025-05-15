pipeline {
    agent any

    stages {
        stage("Checkout") {
            steps {
                sh "rm -rf /*"
                git url: 'https://github.com/ByJeanCa/web-app-test', credentialsId: 'git-token', branch: 'main'
            }
        }
        stage("TESTING code") {
            steps {
                sh "docker compose -f compose_test.yml up --build --abort-on-container-exit"
                sh "docker compose -f compose_test.yml down"
            }
        }
    }
}