# sms_app
This python script reads phone number from a json file and sends sms to those phone numbers using Twilio's API.

Some initial considerations:
* Inside send_sms.py file you should add the following information:
 => Your Twilio Account SID from twilio.com/console
 => Your Auth Token from twilio.com/console
 => You must assign your Twilio phone number to "from_" argument.

* It's possible that you get an error due to phone numbers in the json file are not allowed to in list

Instructions:

1. install virtual environment:
  py venv venv

2. install requirements file:
  pip install -r requirements.txt

3. run the script file:
  py send_sms.py