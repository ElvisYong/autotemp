import json
import requests
import random
from datetime import date, datetime, timedelta

def autotemp(event, context):
    API_ENDPOINT = "https://temptaking.ado.sg/group/MemberSubmitTemperature"
    # too lazy to keep this somewhere
    a = 35.8
    b = 36.9

    # ranndomize the temperature
    temperature = random.randint(a*10, b*10)/10

    # get today's date
    today = date.today()
    # dd/mm/yyyy
    today_formatted = today.strftime("%d/%m/%Y")

    now = datetime.now() + timedelta(hours=8)
    # will only show AM or PM
    current_timeframe = now.strftime("%p")

    # Fill up the payload
    payload = {
      'groupCode': '',
      'date': today_formatted,
      'meridies': current_timeframe,
      'memberId': '',
      'temperature': temperature,
      'pin': '',
    }

    request = requests.post(url=API_ENDPOINT, data=payload)

    return {
        'StatusCode': request.status_code,
    }