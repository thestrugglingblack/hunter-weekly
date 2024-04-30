from twilio.rest import Client
import boto3
import json
import os


def lambda_handler(event, context):
    arn = os.getenv('SECRET_ARN')
    client = boto3.client('secretsmanager')
    res = client.get_secret_value(SecretId=arn)
    secret = json.loads(res['SecretString'])

    account_sid = secret['ACCOUNT_SID']
    auth_token = secret['AUTH_TOKEN']
    twilio_phone_number = secret['TWILIO_PHONE_NUMBER']
    family_members = secret['FAMILY_MEMBERS']
    google_meet_link = secret['GOOGLE_MEET_LINK']

    client = Client(account_sid, auth_token)

    print('About to send message to the Hunter Weekly Family!')
    try:
        print('Running the loop to send messages to family members')
        for member in family_members:
            message_body = f"Hi {member['NAME']}! This is Zuri! Yeah, I know not my actual number but I wrote some code to automate this...pretty cool! Yea I know! Just wanted to let you know the HUNTER family weekly video call is now! Here's the Google Meet link: {google_meet_link}"
            message = client.messages.create(
                body=message_body,
                from_=twilio_phone_number,
                to=member['NUMBER']
            )
            print(f'Message sent to family member:{member["NAME"]} at this number {member["NUMBER"]} !')

        print(f"Message sent to {member['NAME']} at {member['NUMBER']}: {message.sid}... TIME: {message.date_sent}")
    except Exception as e:
        print(f'Failed to send message: {e}')
