# sms_app
This python script reads phone number from a json file and sends sms to those phone numbers using Twilio's API.

# Instructions:

1. Add you auth information to the "send_sms.py" file:
   + Your Twilio Account SID from twilio.com/console
   + Your Auth Token from twilio.com/console
   + You must assign your Twilio phone number to "from_" argument.

2. install virtual environment:
  ```sh
  py venv venv
  ```
    

3. install requirements file:
  ```sh
  pip install -r requirements.txt
  ``` 

4. run the script file:
  ```sh
  py send_sms.py
  ```

# Note: 
It's possible that you get an error due to phone numbers in the json file are not allowed to be sent sms from your account. You could add your own phone number for testing purposes.
