import requests
from datetime import datetime

USERNAME = "" #We create it. So we can give any alphanumeric string
TOKEN = "" #We create it. So we can give any alphanumeric string
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
#After user is created we no longes need this
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id" : GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Days",
    "type": "int",
    "color": "shibafu"
}

headers = {
"X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint,json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today_date = datetime.now()
print(today_date.strftime("%Y%m%d"))  #This is for today , for any other day-> datetime(year=2023, month=8, day=16) instead of datetime.now()

yesterday_date = datetime(year=2023, month=9, day=9)

pixel_data={
    "date": yesterday_date.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code?\n")
}
pixel_headers = {
"X-USER-TOKEN": TOKEN
}

response = requests.post(url=pixel_endpoint,json=pixel_data, headers=pixel_headers)
print(response.text)

date_to_update = yesterday_date.strftime("%Y%m%d")
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_update}/"

pixel_data_update = {
"quantity": "4"
}
# response = requests.put(url=pixel_update_endpoint,json=pixel_data_update, headers=pixel_headers)
# print(response.text)

# requests.delete(url=pixel_update_endpoint,headers=pixel_headers)