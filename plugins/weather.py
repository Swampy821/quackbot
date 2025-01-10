import requests
from requests import RequestException

from cloudbot import hook
from cloudbot.util import colors, database, web

@hook.command("weather", "we", autohelp=False)
def weather(text, reply):
    """<zip> - Gets weather data for <zip>."""

    ds_key = "f01b2c0b0073c5a319173f1e408fb52e"

    with requests.get("https://api.openweathermap.org/data/2.5/weather?zip={}&appid={}&units=imperial".format(text, ds_key)) as response:
        response.raise_for_status()
        data = response.json()

    res = "The weather in {} is {}° and {}".format(data["name"], data["main"]["temp"], data["weather"][0]["description"]);

    return res
