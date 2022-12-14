@Library('python-jenkins-library')_
def version
pipeline {
    agent any
    stages{
        stage("chkVersion"){
            steps{
                script{
                    version = chkVersion()
                }
            }
        }
        stage("prntVersion"){
            steps{
                script{
                    echo "$version"
                }
            }
        }
    }
}