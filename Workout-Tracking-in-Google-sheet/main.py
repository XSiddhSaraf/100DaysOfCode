import requests
from datetime import datetime
import os

GENDER = "Male"
AGE = "34"
WEIGHT_KG = 98
HEIGHT_CM = 182

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = ""
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
TOKEN = os.environ.get("TOKEN")

exercise_text = input("Tell me which exercises you did: ")

headers = {
"x-app-id": APP_ID,
"x-app-key": API_KEY,
"Content-Type": "application/json"
}

bearer_header = {
"Authorization": f"Bearer {TOKEN}"

}
parameters = {
 "query":exercise_text,
 "gender": GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm": HEIGHT_CM,
 "age":AGE
}

response = requests.post(url=EXERCISE_ENDPOINT, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

print(f"Today's date is {today_date}")
print(f"Now time is {now_time}")

for exercise in result['exercises']:
    sheet_input = {
        "workout":{
            "date": today_date,
            "time": now_time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']

        }

    }
    sheet_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_input, headers=bearer_header)
    print(sheet_response.text)
