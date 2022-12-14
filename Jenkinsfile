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
    }
}