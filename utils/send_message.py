from twilio.rest import Client
import os
from django.conf import settings


class SmsTemplates:
    @staticmethod
    def send_otp(otp):
        template = getattr(settings, 'OTP_TEMPLATE', "your verification code is %s")
        return template % otp


class SendSms(object):
    """ SMS API """

    def __init__(self):
        """ twilio Credential  initialization """
        self.account_sid = getattr(settings, 'SMS_API_ACCOUNT_SID', 'ACb3ed8d2759f395b16ea37d5ab35aed4f')
        self.auth_token = getattr(settings, 'SMS_API_AUTH_ACCOUNT', '502c0c3f2987d0fa013456c1458f5240')
        self.client = Client(self.account_sid, self.auth_token)
        self.from_num = getattr(settings, 'SMS_API_FROM_NUMBER', '+13343759625')

    def __call__(self, mobile_no=None, body=''):
        """ Sending Sms """
        message = self.client.messages.create(
            force_delivery=True,
            body=body,
            from_=self.from_num,
            to=mobile_no
        )
        return message


send_sms = SendSms()