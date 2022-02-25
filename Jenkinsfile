pipeline {
    agent any
     options {
        copyArtifactPermission('${JOB_NAME}');
    }
    stages {
        stage('login'){

           steps{
              sh '''
              aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 352708296901.dkr.ecr.us-west-2.amazonaws.com
              '''
           }

        }

        stage('Build') {

            steps {
                echo 'Building..'
                sh '''
                cd simple_webserver
                docker build -t web_server_adham:${BUILD_NUMBER} .
                docker tag web_server_adham:${BUILD_NUMBER} 352708296901.dkr.ecr.us-west-2.amazonaws.com/web_server_adham:${BUILD_NUMBER}

                '''
            }
        }
        stage('push'){
           steps{
              sh '''
              docker push 352708296901.dkr.ecr.us-west-2.amazonaws.com/web_server_adham:${BUILD_NUMBER}
              '''
           }

        }


        stage('Test') {
            when{changeRequest()}
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy - dev') {
            steps {
                echo 'Deploying....'
            }
        }
        stage('Deploy - prod') {
            steps {
                echo 'Deploying....'
            }
        }
        stage('Provision') {

            input {
                message "Do you want to proceed for infrastructure provisioning?"
            }
            when { allOf { branch "dev"; changeset "infra/**/*.tf"} }
            steps {
//                 copyArtifacts filter: 'infra/dev/terraform.tfstate', projectName: '${JOB_NAME}'
//                 sh'''
//
//                 cd infra/dev/
//                 terraform init
//                 terraform plan
//                 terraform apply -auto-approve
//
//                 '''
//                 archiveArtifacts artifacts: 'infra/dev/terraform.tfstate', onlyIfSuccessful: true
                echo 'Provisioning....'

            }
        }


    }
      post {

         always {
            emailext body: 'A Test EMail', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], subject: 'Test'
        }

      }
}
