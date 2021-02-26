#!/usr/bin/env python
# -*- coding: utf-8 -*-

from threading import Thread
from time import sleep

import settings
from api_process import Weather
from db_operations import save_record
from ORM.models import WeatherModel


def db_save_timer() -> None:
    while True:
        time_seconds = settings.SAVE_RECORD_TIME * 60
        sleep(time_seconds)

        save_record()


def main() -> None:
    Thread(target=db_save_timer).start()

    while (inp := input(">>> ")) != "exit":
        if inp == 'weather-info':
            city = input("City: ")
            weather = Weather(city=city)

            print(str(weather))
        elif inp == 'db-read-mode':
            record_id = int(input("Type record id: "))
            weather_record = WeatherModel.get(id=record_id)

            message = (
                f"Record ID: {weather_record.id}\n"
                f"City: {weather_record.city}  Country: {weather_record.country}\n"
                f"Weather description: {weather_record.description}\n"
                f"Temperature (Celsius degrees): {weather_record.temperature}\n"
                f"Minimal temperature: {weather_record.min_temperature}\n"
                f"Maximal temperature: {weather_record.max_temperature}\n"
                f"Pressure: {weather_record.pressure}\n"
                f"Humidity: {weather_record.humidity}\n"
            )
            print(message)

        elif inp == 'set-record-save-time':
            time_minutes = int(input("Type record save time: "))

            settings.SAVE_RECORD_TIME = time_minutes
            print("Saved successfully.")
        else:
            print("Unrecognized command.")


if __name__ == '__main__':
    main()
