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
        stage("Create environment") {
            steps {
                script {
                    bat "python -m pip install -r requirements.txt"
                }
            }
        }
        stage("Testing") {
            steps {
                script {
                    bat "pytest Portfolio/API_testing_framework_advanced_level/tests/tests.py"
                }
            }
        }
    }
}
