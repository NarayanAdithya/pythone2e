@Library('python-jenkins-library')_
def version
pipeline {
    agent any
    stages{
        stage("chkVersion"){
            steps{
                version = chkVersion()
            }
        }
        stage("prntVersion"){
            steps{
                echo "$version"
            }
        }
    }
}