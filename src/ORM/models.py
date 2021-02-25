#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pony import orm

from app.src import settings


database = orm.Database()
database.bind('sqlite', settings.DB_PATH, create_db=True)


class WeatherRecord(database.Entity):
    id = orm.PrimaryKey(int, auto=True)

    city = orm.Required(str)
    country_name = orm.Required(str)
    description = orm.Required(str)

    temperature_c = orm.Required(float)
    min_temperature = orm.Required(float)
    max_temperature = orm.Required(float)

    pressure = orm.Required(float)
    humidity = orm.Required(int)


database.generate_mapping(create_tables=True)
