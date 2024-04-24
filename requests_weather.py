"""
This file is for our new theme: Receives weather information for a given city
Create by: Miqayel Postoyan
Date: 24 April
"""
import requests
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--city", required=True, help="Enter to city")
    parser.add_argument("-w", "--weather", default="all",
                        choices=["all", "temp", "main", "pressure", "humidity", "temp_min", "temp_max"], help="")

    args = parser.parse_args()
    city = args.city
    weather1 = args.weather
    return city, weather1


def print_weather(api, city, weather1, x):
    print("city", city)
    if weather1 == "all":
        print("main: ", x["weather"][0]["main"])
        print("description: ", x["weather"][0]["description"])
        print("temp: ", x["main"]["temp"], "°C")
        print("temp_min: ", x["main"]["temp_min"], "°C")
        print("temp_max: ", x["main"]["temp_max"], "°C")
        print("pressure: ", x["main"]["pressure"])
        print("humidity: ", x["main"]["humidity"])
    elif weather1 == "temp":
        print("temp: ", x["main"]["temp"], "°C")
    elif weather1 == "main":
        print("main: ", x["weather"][0]["main"])
        print("description: ", x["weather"][0]["description"])
    elif weather1 == "pressure":
        print("pressure: ", x["main"]["pressure"])
    elif weather1 == "humidity":
        print("humidity: ", x["main"]["humidity"])
    elif weather1 == "temp_min":
        print("temp_min: ", x["main"]["temp_min"], "°C")
    elif weather1 == "temp_max":
        print("temp_max: ", x["main"]["temp_max"], "°C")


def openWeatherMap(api, city, weather1):
    params = {"q": city, "appid": api, "units": "metric"}
    r = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
    x = r.json()
    try:
        print_weather(api, city, weather1, x)
    except:
        print("There is no such city")

def main():
    city, weather1 = get_arguments()
    api = "be5e83e9b9e390551ebd083e4bff8bf5"
    openWeatherMap(api, city, weather1)


if __name__ == "__main__":
    main()
