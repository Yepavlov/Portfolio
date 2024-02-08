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
        stage("Prepare environment") {
            steps {
                script {
                    dockerImage = docker.build('my_app')
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Define a variable 'runArgs' for the Docker run arguments.
                    // '--rm': Remove the container after it exits.
                    // '-v %cd%:/app': Mount the current Jenkins workspace (%cd%) into the '/app' directory in the container.
                    // '-w /app': Set the working directory inside the container to /app.
                    def runArgs = "--rm -v %cd%:/app -w /app"

                    def testCmd = "python -m pytest --alluredir=allure-results"

                    // Run the Docker container with the specified arguments and command.
                    bat "docker run ${runArgs} my-app ${testCmd}"
                }
            }
        }
    }
    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}
