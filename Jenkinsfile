@Library('python-app-library')_
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
        stage("versionIncrement"){
            steps{
                script{
                    incrementVersion("dev")
                    version=getVersion()
                }
            }
        }
        stage("Commit Version Update"){
            steps{
                script{
                    makeupdatecommit("Pythone2e")
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