import json
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client

TWILIO_ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
TWILIO_AUTH_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
TWILIO_PHONE_NUMBER = "XXXXXXXXXXX"

def main():
# Your Account SID from twilio.com/console
  account_sid = TWILIO_ACCOUNT_SID
# Your Auth Token from twilio.com/console
  auth_token  = TWILIO_AUTH_TOKEN
  
  with open("./phones.json", "r") as file:
    try:
      phone_list = json.load(file)['numbers']
          
    except json.decoder.JSONDecodeError:
      print("There was a problem accessing the data.")

  try:
    client = Client(account_sid, auth_token)

    for number in range(len(phone_list)):
      message = client.messages.create(
        to=phone_list[number], 
        from_=TWILIO_PHONE_NUMBER,
        body="Hello from Python!")

      print(message.sid)

  except TwilioRestException as e:
    print(e)

if __name__ == "__main__":
    main()  