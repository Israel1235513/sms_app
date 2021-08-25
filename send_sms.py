import json
import twilio
from twilio.rest import Client

def main():
# Your Account SID from twilio.com/console
  account_sid = "ACd4412acfa14769f101c8446584f360de"
# Your Auth Token from twilio.com/console
  auth_token  = "04e27d45a18334568bc809b595efdc42"
  
  with open("./phones.json", "r") as file:
    try:
      phone_list = json.load(file)['numbers']
          
    except json.decoder.JSONDecodeError:
      print("There was a problem accessing the data.")


  try:
    client = Client(account_sid, auth_token)

    for i in range(len(phone_list)):
      message = client.messages.create(
        to=phone_list[i], 
        from_="+18506085264",
        body="Hello from Python!")

      print(message.sid)

  except twilio.TwilioRestException as e:
    print(e)

if __name__ == "__main__":
    main()  