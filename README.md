```text

 __  __  __  __  __   __  ______  ______  ______       __     __  ______  ______  __  __   __      __  __    
/\ \_\ \/\ \/\ \/\ "-.\ \/\__  _\/\  ___\/\  == \     /\ \  _ \ \/\  ___\/\  ___\/\ \/ /  /\ \    /\ \_\ \   
\ \  __ \ \ \_\ \ \ \-.  \/_/\ \/\ \  __\\ \  __<     \ \ \/ ".\ \ \  __\\ \  __\\ \  _"-.\ \ \___\ \____ \  
 \ \_\ \_\ \_____\ \_\\"\_\ \ \_\ \ \_____\ \_\ \_\    \ \__/".~\_\ \_____\ \_____\ \_\ \_\\ \_____\/\_____\ 
  \/_/\/_/\/_____/\/_/ \/_/  \/_/  \/_____/\/_/ /_/     \/_/   \/_/\/_____/\/_____/\/_/\/_/ \/_____/\/_____/ 
                                                                                                            
```
## Table of Contents
* [Overview](#overview)
* [Pre-requisites](#pre-requisites)
* [Project Structure](#project-structure)
* [Setup](#setup)
* [Deployment](#deployment)
* [Testing](#testing)
* [Lessons Learned](#lessons-learned)

## Overview
**Hunter Weekly** is a weekly notification task that sends a text message to a group of family members notifiying them of our weekly family video calls. This project is supported with AWS and Twilio. It uses Twilio SMS to send text messages to the family member and AWS to run the script every Wednesday at 9 PM EST. The AWS resources is deployed with AWS-CDK.

## Pre-requisites
* [NVM](https://github.com/nvm-sh/nvm)
* [Node.js v20]()
* [Python v3.8](https://www.python.org/downloads/release/python-380/)
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
* [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html#getting_started_install)
* [Twilio SMS](https://www.twilio.com/docs/messaging/tutorials/how-to-send-sms-messages/python)

## Setup
1. Run `nvm use` for the correct version of Node.js.
2. Run `npm install -g aws-cdk` to install the AWS CDK.
3. Run `export AWS_PROFILE=profile_name` to set the AWS profile.
> Note: Programmatically update cdk.json property `profile` to the name of the AWS profile.
4. Create **.env** file with the following properties:
```text
EMAIL=YOUR_EMAIL
```
5. Run `python3 -m venv .venv` to create a virtual environment.
6. Run `source .venv/bin/activate` to activate the virtual environment.
7. Run `pip install -r requirements.txt` to install the required dependencies.

## Deployment
In order for the project to kick off these are the required secrets needed in AWS Secrets Manager:
* `TWILIO_ACCOUNT_SID`
* `TWILIO_AUTH_TOKEN`
* `TWILIO_PHONE_NUMBER`
* `GOOGLE_MEET_LINK`

The `FAMILY_MEMBERS` property is a comma separated list of phone numbers that will receive the text message following this format
```json
{
  "NAME": "John Doe",
  "NUMBER": "+1234567890"
}
```

To deploy the project run the following commands:
1. Run `cdk diff` to see the changes that will be made.
2. Run `cdk deploy` to deploy the project.
3. Go to your email and confirm the subscription to the SNS topic.

## Testing
Run `python -m unittest` to run the tests.

## Lessons Learned
* To add a layer for Python dependencies the file path that needs to be compressed must follow a file structure of `python/{NAME_OF_LIBRARY}`
* By default Lambda functions are deployed with a 512MB memory limit. This can be increased to 3GB.
* By default Lambda functions are deployed with a 15 second timeout. This can be increased to 15 minutes. For this project I had to increase to 5 minutes.
* To compress the code for the Lambda function you must have the contents needed in the file. If there is an extra folder or path it will need to be updated in the `handler` prop for the Lambda AWS-CDK construct.
* Twilio numbers must be sent as a string with the country code. For example `+1234567890`.