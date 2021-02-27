#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

# DB
DB_PATH = f'{Path().absolute()}/weather.sqlite'

# Weather
CITY = 'Warsaw'  # This city's records will be saved to the database

# Time
SAVE_RECORD_TIME = 10  # Time in minutes
