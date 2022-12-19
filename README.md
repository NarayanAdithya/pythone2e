# Production
[![Build Status](http://64.227.128.144:8080/buildStatus/icon?job=PythonE2E%2Fmain)](http://64.227.128.144:8080/job/PythonE2E/job/main/)

# Stage
[![Build Status](http://64.227.128.144:8080/buildStatus/icon?job=PythonE2E%2Fstage)](http://64.227.128.144:8080/job/PythonE2E/job/stage/)

# Dev
[![Build Status](http://64.227.128.144:8080/buildStatus/icon?job=PythonE2E%2Fdev)](http://64.227.128.144:8080/job/PythonE2E/job/dev/)

<h1 align="center"> About </h1>

This project aims to implement a standard CI/CD pipeline for a Flask project whose dependencies are managed using Poetry. A basic flask application has been made and it has a `version.toml` file that is used for storing and keeping track of the version. The code in `utils/versioner.py` is used to bump the version and it accepts three arguments `--dev` for patch update, `--stage` for minor update and `--main` for major update. 

<h1 align="center"> Stages in CI Pipeline and Associated Commands </h1>

1. Install Environment - `python3 -m venv env && source env/bin/activate`
2. Install Dependencies - `pip install -r devrequirements.txt`
3. Run Linting - `python3 -m flake8 .`
4. Run Unit Test - `python3 -m  pytest .`
5. Bump Version - `python3 utils/versioner.py --dev`
6. Commit Version Update and Push Changes
7. Build Docker Image from Dockerfile
8. Docker Login
9. Push Image to DockerHub Repository

<h1 align="center"> Jenkins </h1>

A multibranch project has been setup with a Multibranch webhook trigger setup to build the latest release on a commit. The Jenkins has also been configured with Build Trigger Extension to prevent build on certain file changes like README.md etc. The Embeddable Status Plugin was used to create the badge shown on the top of the README.md file. Jenkins is making use of custom defined library for normal python build commands. These repo's can be found <a href="https://github.com/NarayanAdithya/python-jenkins-shared-library"> here </a>.
