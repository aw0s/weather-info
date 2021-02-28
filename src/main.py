#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from threading import Thread
from time import sleep

from pony.orm import db_session

import settings
from api_process import Weather
from db_operations import save_record
from models import WeatherModel


def db_save_timer() -> None:
    while True:
        save_record()

        time_seconds = settings.SAVE_RECORD_TIME * 60
        sleep(time_seconds)


def main() -> None:
    Thread(target=db_save_timer).start()

    if len(argv) > 1:
        command = argv[1]

        if command == 'weather-info':
            city = input("City: ")

            try:
                weather = Weather(city=city)
                print(str(weather))
            except AttributeError:
                print("Weather API couldn't find any city satisfying your requirements.")
        elif command == 'db-read-mode':
            record_id = int(input("Type record id: "))

            with db_session:
                weather_record = WeatherModel.get(id=record_id)

            message = (
                f"Record ID: {weather_record.id}\n"
                f"City: {weather_record.city}  Country: {weather_record.country}\n"
                f"Weather description: {weather_record.description}\n"
                f"Temperature (Celsius degrees): {weather_record.temperature_c}\n"
                f"Minimal temperature: {weather_record.min_temperature}\n"
                f"Maximal temperature: {weather_record.max_temperature}\n"
                f"Pressure: {weather_record.pressure}\n"
                f"Humidity: {weather_record.humidity}\n"
            )
            print(f"\n{message}")
        else:
            print("Unrecognized command.")

    print("\nCollecting data mode.")


if __name__ == '__main__':
    main()
