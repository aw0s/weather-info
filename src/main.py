#!/usr/bin/env python
# -*- coding: utf-8 -*-

import api_process


def main() -> None:
    # print(api_process.get_api_dict(api_call='http://api.openweathermap.org/data/2.5/weather?q=Warsaw&appid='))

    # while inp := input("<<< ") != "exit":

    weather = api_process.Weather(city='Świdnik')
    weather.database_connection_init()
    weather.save_weather_record()

    print(weather.humidity)


if __name__ == '__main__':
    main()
