from twilio.rest import Client
import os

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
phone_number_to_call = os.environ['PHONE_NUMBER_TO_CALL']
twilio_phone_number = os.environ['TWILIO_PHONE_NUMBER']
twiml_path = os.environ['TWIML_PATH']


def lambda_handler(event, context):
    client = Client(account_sid, auth_token)
    call = client.api.account.calls.create(to=phone_number_to_call,
                                           from_=twilio_phone_number,
                                           url=twiml_path,
                                           method="GET",
                                           record="false")
