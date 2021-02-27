#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pony import orm as ponyorm

import settings
from api_process import Weather
from models import WeatherModel


class WeatherSave(Weather):
    def __init__(self, city: str):
        super().__init__(city)

        self.database = ponyorm.Database()

    def database_connection_init(self) -> None:
        self.database.bind('sqlite', settings.DB_PATH, create_db=True)
        self.database.generate_mapping(create_tables=True)

    @ponyorm.db_session
    def save_weather_record(self) -> None:
        WeatherModel(
            city=self.city,
            country=self.country,
            description=self.weather_description,
            temperature_c=self.temperature_c,
            min_temperature=self.min_temperature,
            max_temperature=self.max_temperature,
            pressure=self.pressure,
            humidity=self.humidity,
        )
        ponyorm.commit()


def save_record() -> None:
    weather_save = WeatherSave(city=settings.CITY)
    weather_save.database_connection_init()
    weather_save.save_weather_record()
