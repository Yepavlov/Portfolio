pipeline {
    agent any

    stages {
        stage ("Clone repository") {
            steps {
                git branch: "main", url: "https://github.com/Yepavlov/Portfolio.git"
            }
        stage ("Create environment") {
            steps {
                bat "python -m pip install -r requirements.txt"
            }
        }
        stage("Testing") {
            steps {
                bat "pytest Portfolio/API_testing_framework_advanced_level/tests/tests.py"
            }
        }

        }
    }



}