pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Ansarey/python-test.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Install Script') {
            steps {
                // Assuming 'install-dependencies' is a shell script
                sh 'bash install-dependencies'
            }
        }
        stage('Run Application') {
            steps {
                // Run your application or any test scripts here
                sh 'python app.py'
            }
        }
        stage('Deploy') {
            steps {
                // Add your deployment steps here
                echo 'Deploying application...'
                // You might need to use a deployment script or commands here
                // sh 'bash deploy.sh' (example, if you have a deployment script)
            }
        }
    }
    post {
        always {
            echo 'Pipeline completed.'
        }
    }
}
