import requests
import os
from dotenv import load_dotenv
import csv
import datetime as dt

load_dotenv()

APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']

WEIGHT_KG = 73
HEIGHT_CM = 188
AGE = 27
GENDER = 'male'

# Supported activities:
# Running/Jogging - "ran for 30 minutes", "jogged 2 miles"
# Swimming - "swam for 1 hour", "swimming laps"
# Walking - "walked 3 miles", "brisk walk 45 min"
# Cycling - "biked for 1 hour", "rode bike 10 miles"
# Weightlifting - "lifted weights 45 min", "weight training"

exercise = input('Which exercises you did ?: ')

url = 'https://app.100daysofpython.dev/v1/nutrition/natural/exercise'

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

data = {
    'query': exercise,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE,
    'gender': GENDER,
}

response = requests.post(url, headers=headers, json=data)
result = response.json()

today = dt.datetime.now()

date = today.strftime('%d/%m/%Y')
time = today.strftime('%H:%M:%S')

for exercise in result['exercises']:
    print(exercise['name'])
    print(exercise['duration_min'])
    print(exercise['nf_calories'])


    with open('workouts.csv', mode='a', newline='') as file:
        writer = csv.writer(file)

        writer.writerow([date, time, exercise['name'], exercise['duration_min'], exercise['nf_calories']])