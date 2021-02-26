#!/usr/bin/env python
# -*- coding: utf-8 -*-

import schedule

import settings
from api_process import Weather
from db_operations import WeatherSave


def save_record() -> None:
    weather_save = WeatherSave(city=settings.CITY)
    weather_save


def main() -> None:
    schedule.every().minute.do(save_record)

    while inp := input("<<< ") != "exit":
        if inp == 'weather-info':
            pass
        elif inp == 'db-read-mode':
            pass
        elif inp == 'set-scheduler':
            pass
        else:
            print("Unrecognized command.")


if __name__ == '__main__':
    main()
