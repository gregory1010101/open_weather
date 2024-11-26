import requests

r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Ufa&units=metric&lang=ru&APPID=b5798fea07f30825fd1ab229e85beccb').json()
print("Долгота:", r["coord"]["lon"], "с.ш.")
print("Широта:", r["coord"]["lat"], "в.д.")
print("Город:", r["name"])
print("Сейчас:", r["weather"][0]["description"])
print("Температура:", r["main"]["temp"], "℃")
print("Ощущается как:", r["main"]["feels_like"], "℃")
print("Ветер:", r["wind"]["speed"], "м/с")
print("Давление:", (r["main"]["pressure"] * 0.76), "мм.рт.ст.")
print("Относительная влажность:", r["main"]["humidity"], "%")