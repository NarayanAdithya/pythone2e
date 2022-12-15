@Library('python-app-library')_
pipeline {
    agent any
    stages{
        stage("createvenv"){
            steps{
                script{
                    makeEnv()
                }
            }
        }
        stage("installDeps")
        {
            steps{
                script{
                    activateEnv()
                    installDependencies()
                }
            }
        }
        stage("linting"){
            steps{
                script{
                    
                    linter()
                }
            }
        }
        stage("testing"){
            steps{
                script{
                    
                    testCases()
                }
            }
        }
        stage("Build Image"){
            steps{
                script{
                    buildDockerImage()
                }
            }
        }
        stage("Login"){
            steps{
                script{
                    dockerLogin()
                }
            }
        }
        stage("Push Artifact"){
            steps{
                script{
                    dockerPush()
                }
            }
        }
    }
}