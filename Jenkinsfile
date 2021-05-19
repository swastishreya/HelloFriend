pipeline {
    environment {
        dockerImage = ""
    }
    agent any

    stages {
        stage('Step1: Git pull:Frontend') {
            steps {
                git 'https://github.com/brahmakulkarni/SPE_Project_Frontend'
            }
        }
        stage('Step2: Install npm dependencies:Frontend') {
            steps {
                sh 'npm install'
            }
        }
        stage('Step3: Test:Frontend') {
            steps {
                sh 'CI=true npm run test a'
            }
        }
        stage('Step4: Building docker image:Frontend') {
            steps {
                script {
                    dockerImage = docker.build "brahma99/hellofriendfrontend:latest"
                }
            }
        }
        stage('Step5: Push Docker image to Docker Hub:Frontend') {
            steps {
                script {
                    docker.withRegistry('', 'docker-jenkins') {
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Step6: Git pull:Backend') {
            steps {
                git branch: 'main', url: 'https://github.com/swastishreya/HelloFriend'
            }
        }
        stage('Step7: Set up environment:Backend') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Step8: Test:Backend') {
            steps {
                sh 'python3 -m pytest'
            }
        }
        stage('Step9: Building docker image:Backend') {
            steps {
                script {
                    dockerImage = docker.build "swastishreya/hellofriendbackend:latest"
                }
            }
        }
        stage('Step10: Push Docker image to Docker Hub:Backend') {
            steps {
                script {
                    docker.withRegistry('', 'docker-jenkins-swasti') {
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Step11: Ansible pull image') {
            steps {
                ansiblePlaybook becomeUser: null, colorized: true, disableHostKeyChecking: true, installation: 'Ansible', inventory: 'docker_deployment/inventory', playbook: 'docker_deployment/deploy_docker.yml', sudoUser: null
            }
        }
    }
}

