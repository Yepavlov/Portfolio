pipeline {
    agent any

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
                    bat "python -m pytest rest_api_testing_framework_notes_swagger\\tests\\"
                }
            }
        }
    }
}
