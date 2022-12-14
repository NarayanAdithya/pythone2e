@Library('python-jenkins-library')_
def version
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
        stage("Increment Version"){
            steps{
                script{
                    incrementVersion()
                    version = getVersion()
                }
            }
        }
        stage("Build Image"){
            steps{
                script{
                    buildDockerImage(version)
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
                    dockerPush(version)
                }
            }
        }
    }
}