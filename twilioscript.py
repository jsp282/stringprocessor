from twilio.rest import TwilioRestClient

ACCOUNT_SID = "AC6c6cae123c1e1b437007fc66017889aa"
ACCOUNT_SID = "ACa68b97327cd0c632838492a1ba460e1e"
#ACCOUNT_SID = "AC5ef872f6da5a21de157d80997a64bd33"
AUTH_TOKEN = "e4c811742700663592056e25d4643706"
AUTH_TOKEN ="c7ad22628986cd406373f9b152559f8e"
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
client.messages.create(
    to_="+16462360202",
    from_="+13478366402",
    body="Subscribed to String Blockchain" 
)
