import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
verify = client.verify.services(os.environ['TWILIO_VERIFY_SERVICE_SID'])


def send(phone):   #sending code 
    verify.verifications.create(to=phone, channel='sms')


def check(phone, code):    #matching the phone number and code which twilio sent
    try:
        result = verify.verification_checks.create(to=phone, code=code)
    except TwilioRestException:
        print('no')
        return False
    return result.status == 'approved'
