#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pony import orm as ponyorm

import settings
from api_process import Weather
from ORM.models import WeatherRecord


class WeatherSave(Weather):
    def __init__(self, city: str):
        super().__init__(city)

        self.data = ponyorm.Database()

    def database_connection_init(self) -> None:
        self.database.bind('sqlite', settings.DB_PATH, create_db=True)
        self.database.generate_mapping(create_tables=True)

    @ponyorm.db_session
    def save_weather_record(self) -> None:
        WeatherRecord(
            city=self.city,
            country_name=self.country_name,
            description=self.weather_description,
            temperature_c=self.temperature_c,
            min_temperature=self.min_temperature,
            max_temperature=self.max_temperature,
            pressure=self.pressure,
            humidity=self.humidity,
        )
        ponyorm.commit()
