#!/usr/bin/env python
# -*- coding: utf-8 -*-

from json import loads
from os import getenv

from dotenv import load_dotenv
from requests import get


load_dotenv()
API_KEY = getenv('API_KEY')


def get_api_dict(api_call: str) -> dict:
    api_dict = dict(loads(get(api_call).text))

    return api_dict


class Weather:
    def __init__(self, city: str) -> None:
        self.city = city

        self.api_call = f'api.openweathermap.org/data/2.5/weather?q={self.city}&appid={API_KEY}'
        self.api_dict = get_api_dict(self.api_call)


