#!/usr/bin/env python
# -*- coding: utf-8 -*-

from json import loads
from os import getenv

from dotenv import load_dotenv
from pony import orm as ponyorm
from requests import get

import settings
from utils import kelvin_to_celsius


load_dotenv()
API_KEY = getenv('API_KEY')


def get_api_dict(api_call: str) -> dict:
    api_dict = dict(loads(get(api_call).text))

    return api_dict


class Weather:
    def __init__(self, city: str) -> None:
        self._city = city

        self.api_call = f'http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={API_KEY}'
        self.api_dict = get_api_dict(self.api_call)

        self.country = self.api_dict.get('sys').get('country')
        self.weather_description = self.api_dict.get('weather')[0].get('description')

        api_dict_main = self.api_dict.get('main')
        temperature_k = api_dict_main.get('temp')
        self.temperature_c = round(kelvin_to_celsius(temperature_k), 1)
        self.min_temperature = round(kelvin_to_celsius(api_dict_main.get('temp_min')), 1)
        self.max_temperature = round(kelvin_to_celsius(api_dict_main.get('temp_max')), 1)

        self.pressure = api_dict_main.get('pressure')
        self.humidity = api_dict_main.get('humidity')

        self.database = ponyorm.Database()

    @property
    def city(self) -> str:
        return self._city

    @city.getter
    def city(self) -> str:
        if self._city.strip():
            return self._city
        else:
            return settings.CITY

    @city.setter
    def city(self, value: str) -> None:
        self._city = value

    def __str__(self) -> str:
        return (
            f"City: {self.city}  Country: {self.country}\n"
            f"Weather description: {self.weather_description}\n"
            f"Temperature (Celsius degrees): {self.temperature_c}\n"
            f"Minimal temperature: {self.min_temperature}\n"
            f"Maximal temperature: {self.max_temperature}\n"
            f"Pressure: {self.pressure}\n"
            f"Humidity: {self.humidity}\n"
        )
