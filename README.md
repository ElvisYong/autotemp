# Steps to upload to aws lambda using serverless

## Install serverless
Install with npm
```
npm install -g serverless
```

## Create an IAM User and Access Key
1. Login to your AWS account and go to the Identity & Access Management (IAM) page.

2. Click on Users and then Add user. Enter a name in the first field to remind you this User is related to the Serverless Framework, like serverless-admin. Enable Programmatic access by clicking the checkbox. Click Next to go through to the Permissions page. Click on Attach existing policies directly. Search for and select AdministratorAccess then click Next: Review. Check to make sure everything looks good and click Create user.

3. View and copy the API Key & Secret to a temporary place. You'll need it in the next step.

### Quick setup
```
export AWS_ACCESS_KEY_ID=<your-key-here>
export AWS_SECRET_ACCESS_KEY=<your-secret-key-here>
# AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY are now available for serverless to use
serverless deploy
```
More info: https://www.serverless.com/framework/docs/providers/aws/guide/credentials/

## Create serverless.yml in a working directory
See [severless.yml](https://github.com/ElvisYong/autotemp/blob/master/serverless.yml)

## Setup Virtualenv and requirements.txt

Install and activate virtualenv
```
$pip install virtualenv
$virtualenv venv
$source venv/bin/activate
```

Install required dependencies and save to requirements.txt
```
(venv) $pip install flask
(venv) $pip freeze > requirements.txt
```

## Deploy Serverless

Deploy the function
```
$sls deploy
```

Test invoke the function
```
$sls invoke -f autotemp
```

More info: https://www.serverless.com/blog/flask-python-rest-api-serverless-lambda-dynamodb