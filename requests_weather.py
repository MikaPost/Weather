"""
This file is for our new theme: Receives weather information for a given city
Create by: Miqayel Postoyan
Date: 30 April
"""
import requests
import argparse


def get_arguments():
    """
    Function: get_arguments
    Brief: get arguments argparse
    Params: None
    Return:	city, weather1
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--city", required=True, help="Enter to city")
    parser.add_argument("-w", "--weather", default="all",
                        choices=["all", "temp", "main", "pressure", "humidity", "temp_min", "temp_max"], help="")

    args = parser.parse_args()
    city = args.city
    weather1 = args.weather
    return city, weather1


def print_weather(city, weather1, request_json):
    """
    Function: print_weather
    Brief: print weather
    Params: city, weather1, request_json
    Return:	None
    """
    print("city", city)
    if weather1 == "all":
        print("main: ", request_json["weather"][0]["main"])
        print("description: ", request_json["weather"][0]["description"])
        print("temp: ", request_json["main"]["temp"], "°C")
        print("temp_min: ", request_json["main"]["temp_min"], "°C")
        print("temp_max: ", request_json["main"]["temp_max"], "°C")
        print("pressure: ", request_json["main"]["pressure"])
        print("humidity: ", request_json["main"]["humidity"])
    elif weather1 == "temp":
        print("temp: ", request_json["main"]["temp"], "°C")
    elif weather1 == "main":
        print("main: ", request_json["weather"][0]["main"])
        print("description: ", request_json["weather"][0]["description"])
    elif weather1 == "pressure":
        print("pressure: ", request_json["main"]["pressure"])
    elif weather1 == "humidity":
        print("humidity: ", request_json["main"]["humidity"])
    elif weather1 == "temp_min":
        print("temp_min: ", request_json["main"]["temp_min"], "°C")
    elif weather1 == "temp_max":
        print("temp_max: ", request_json["main"]["temp_max"], "°C")


def open_weather_map(api, city, weather1):
    """
    Function: openWeatherMap
    Brief: openWeatherMap api
    Params: api, city, weather1
    Return:	def print_weather
    """
    params = {"q": city, "appid": api, "units": "metric"}
    request = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
    request_json = request.json()
    try:
        print_weather(city, weather1, request_json)
    except:
        print("There is no such city")


def main():
    """
    Function: main
    Brief: Entry point
    """
    city, weather1 = get_arguments()
    api = "be5e83e9b9e390551ebd083e4bff8bf5"
    open_weather_map(api, city, weather1)


if __name__ == "__main__":
    main()
