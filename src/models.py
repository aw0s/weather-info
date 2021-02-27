#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pony import orm as ponyorm

import settings

database = ponyorm.Database()
database.bind('sqlite', settings.DB_PATH, create_db=True)


class WeatherModel(database.Entity):
    id = ponyorm.PrimaryKey(int, auto=True)

    city = ponyorm.Required(str)
    country = ponyorm.Required(str)
    description = ponyorm.Required(str)

    temperature_c = ponyorm.Required(float)
    min_temperature = ponyorm.Required(float)
    max_temperature = ponyorm.Required(float)

    pressure = ponyorm.Required(float)
    humidity = ponyorm.Required(int)


database.generate_mapping(create_tables=True)
