from pathlib import Path


# DB
DB_PATH = f'{Path().absolute()}/weather.sqlite'

# Weather
CITY = 'Warsaw'  # This city's records will be saved to the database

# Scheduler
SAVE_RECORD_TIME = 60  # Time in minutes
