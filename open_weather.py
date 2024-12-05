import sys
import requests
from dotenv import load_dotenv
import os

load_dotenv()

my_city = str(sys.argv[1])
par = {
	"lang": os.getenv("MY_LANGUAGE"),
	"q":my_city,
	"appid": os.getenv("API_KEY"),
	"units": "metric"
}

r = requests.get(os.getenv("API_URL"), params = par).json()
print("Город:", r["name"])
print("Сейчас:", r["weather"][0]["description"])
print("Температура:", r["main"]["temp"], "℃")
print("Ощущается как:", r["main"]["feels_like"], "℃")
print("Ветер:", r["wind"]["speed"], "м/с")
print("Давление:", (r["main"]["pressure"] * 0.76), "мм.рт.ст.")
print("Относительная влажность:", r["main"]["humidity"], "%")