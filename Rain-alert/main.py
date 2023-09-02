import requests
from twilio.rest import Client
import os

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = os.environ.get('OWM_API_KEY')
account_sid = "ACf51be69dfcd5e4890047d1969de0c489"
auth_token = os.environ.get('AUTH_KEY')

weather_params = {
    "lat": 18.520430,
    "lon": 73.856743,
    "appid": api_key,
    "exclude" : "current,minutely,daily"

}
response =requests.get(OWM_Endpoint, params=weather_params)
print(response.status_code)
response.raise_for_status()

weather_data = response.json()
hourly_slice = weather_data['hourly'][:12]

will_rain = False

for hour in hourly_slice:
    condition_code = hour['weather'][0]['id']
    if condition_code <= 500:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It is going to rain today. Remember to bring ☔",
        from_= "",
        to=''
    )
    print(message.status)

