pipeline {
  agent any
  stages {
    stage('Print hello') {
      steps {
        echo 'Hello'
      }
    }

    stage('end') {
      steps {
        sh 'batch echo \'done\''
      }
    }

  }
}