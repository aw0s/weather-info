#!/usr/bin/env python
# -*- coding: utf-8 -*-

import api_process


def main() -> None:
    # print(api_process.get_api_dict(api_call='http://api.openweathermap.org/data/2.5/weather?q=Warsaw&appid='))

    # while inp := input("<<< ") != "exit":

    weather = api_process.Weather('Świdnik')
    print(weather.temperature_F)


if __name__ == '__main__':
    main()
