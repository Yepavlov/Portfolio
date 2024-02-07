pipeline {
    agent any
    environment {
        USERS_NAME_NOTES=credentials("name")
        USERS_EMAIL_ADDRESS_NOTES=credentials("email")
        USERS_PASSWORD_NOTES=credentials("password")
        NEW_USERS_PASSWORD_NOTES=credentials("new_password")

    }

    stages {
        stage("Clone repository") {
            steps {
                script {
                    git branch: "main", url: "https://github.com/Yepavlov/Portfolio.git"
                }
            }
        }
        stage("Set path") {
            steps {
                script {
                    env.PATH = "C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python311\\;${env.PATH}"
                }
            }
        }
        stage("Create environment") {
            steps {
                script {
                    bat "python -m pip install -r requirements.txt"
                }
            }
        }
        stage("Update pip") {
            steps {
                script {
                    bat "python -m pip install --upgrade pip"
                }
            }
        }
        stage("Testing") {
            steps {
                script {
                    bat "python -m pytest rest_api_testing_framework_notes_swagger\\tests\\ --junitxml=junit_test_result.xml"
                }
            }
        }
    }
    post {
        always {
            junit "junit_test_result.xml"
        }
    }
}
