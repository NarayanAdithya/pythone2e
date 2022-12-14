@Library('python-jenkins-library')_

pipeline {
    agent any
    environment{
        Version = ''
    }
    stages{
        stage("chkVersion"){
            steps{
                chkVersion()
            }
        }
    }
}