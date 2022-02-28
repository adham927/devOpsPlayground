pipeline {
//     agent { label 'ec2-fleet' }
       agent any
//      options {
//         copyArtifactPermission('${JOB_NAME}');
//     }
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
                ec2-metadata
                echo $USER
                cd simple_webserver
                docker build -t web_server_adham:${BUILD_NUMBER} .
                docker tag web_server_adham:${BUILD_NUMBER} 352708296901.dkr.ecr.us-west-2.amazonaws.com/web_server_adham:${BUILD_NUMBER}

                cd ../package_demo
                python3 setup.py sdist bdist_wheel
                pip3 install twine
                aws codeartifact login --tool twine --repository artifactory-repo-adham --domain adham-repo --domain-owner 352708296901
                python3 -m twine upload dist/* --repository codeartifact
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
//       post {
//          always {
//                mail body: "this message from jenkins just for test configuration", subject: "from jenkins", to: "ad.amer1989@gmail.com";
//          }
//       }
}
