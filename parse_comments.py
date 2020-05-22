import json

import requests

url = "https://lenta.ru/news/2020/05/09/timati/"


def get_data():
    data = {
        "appId": 126,
        "xid": url,
        "comments_sorting": "date_asc"
    }
    response = requests.post('https://c.rambler.ru/api/v2/json/get_comments', json=data)
    with open('data.json', 'w') as f:
        f.write(response.text)


get_data()
