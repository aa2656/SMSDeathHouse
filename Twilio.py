from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)


def sendSms(bodytxt, toNum, fromNum):
    client.messages \
        .create(
        body=bodytxt,
        from_=fromNum,
        to=toNum
    )

def getSms():
    return