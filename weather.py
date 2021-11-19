# Чтобы сформировать список всех пакетов использую:
#
# pip freeze > requirements.txt
# При установке пакетов на новой машине:
#
# pip install -r requirements.txt
# https://habr.com/ru/post/315264/

import requests
s_city = "Petersburg,RU"
city_id = 0
appid = "буквенно-цифровой APPID"
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                 params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
    data = res.json()
    cities = ["{} ({})".format(d['name'], d['sys']['country'])
              for d in data['list']]
    print("city:", cities)
    city_id = data['list'][0]['id']
    print('city_id=', city_id)
except Exception as e:
    print("Exception (find):", e)
    pass