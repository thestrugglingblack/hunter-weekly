import unittest
from unittest.mock import patch, MagicMock
from infra.lambda_func import send_message
class TestSendMessage(unittest.TestCase):

    @patch('boto3.client')
    @patch('twilio.rest.Client')
    def test_lambda_handler(self, mock_twilio, mock_boto3):
        # Mock the response of AWS Secrets Manager
        mock_boto3.return_value.get_secret_value.return_value = {
            'SecretString': '{"ACCOUNT_SID": "test_sid", "AUTH_TOKEN": "test_token", "TWILIO_PHONE_NUMBER": "test_number", "FAMILY_MEMBERS": [{"NAME": "John Doe", "NUMBER": "+1234567890"}], "GOOGLE_MEET_LINK": "test_link"}'
        }

        # Mock the response of Twilio Client
        mock_message = MagicMock()
        mock_message.sid = 'test_sid'
        mock_message.date_sent = 'test_date'
        mock_twilio.return_value.messages.create.return_value = mock_message

        # Call the function to be tested
        send_message.lambda_handler(None, None)

        # Assert that the AWS Secrets Manager was called with the correct parameters
        mock_boto3.return_value.get_secret_value.assert_called_with(SecretId='SECRET_ARN')

        # Assert that the Twilio Client was called with the correct parameters
        mock_twilio.return_value.messages.create.assert_called_with(
            body='Hi John Doe! This is Zuri! Yeah, I know not my actual number but I wrote some code to automate this...pretty cool! Yea I know! Just wanted to let you know the HUNTER family weekly video call is now! Here\'s the Google Meet link: test_link',
            from_='test_number',
            to='+1234567890'
        )

if __name__ == '__main__':
    unittest.main()