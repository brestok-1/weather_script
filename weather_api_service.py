from datetime import datetime
from typing import NamedTuple
from enum import Enum

from coordinates import Coordinates

Celsius = int

key = '909c7b331b35205c8a4b26780af01e47'


class WeatherType(Enum):
    THUNDERSTORM = 'Гроза'
    DRIZZLE = 'Изморозь'
    RAIN = 'Дождь'
    SNOW = 'Снег'
    CLEAR = 'Ясно'
    FOG = 'Туман'
    CLOUDS = 'Облачно'


class Weather(NamedTuple):
    temperature: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str


def get_weather(coordinates: Coordinates) -> Weather:
    '''Requests weather in OpenWeather API and returns it'''
    pass
