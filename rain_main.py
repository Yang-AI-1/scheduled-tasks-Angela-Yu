import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv(".env")
OMW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
api_key = os.getenv("OMW_API_KEY")

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

weather_params = {
    "lat":-1.3026148,
    "lon":36.828842,
    "appid": api_key,
    "cnt": 4,
}
response = requests.get(OMW_Endpoint, params=weather_params) #Supposed to use the.get functionality
response.raise_for_status() #Raises an exception for everything other than a successful response code.
data = response.json()
weather_codes = [dictionary["weather"][0]["id"] for dictionary in data["list"]]
will_rain = False
for code in weather_codes:
    if code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages.create(
        body = "Carry an Umbrella. Its gonna rain!!",
        from_ = "whatsapp:+14155238886",
        to= "whatsapp:+254714938076"
    )
    print(message.status)
else:
    print("No rain predicted, so no message was sent.")
