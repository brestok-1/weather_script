from typing import NamedTuple
import geocoder

import config
from exceptions import CantGetCoordinates


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_coordinates() -> Coordinates:  # -> tuple[float, float]:  Defines what type of data the function should return
    """Returns current coordinates """
    location = geocoder.ip('me')
    if not location.status_code == 200:
        raise CantGetCoordinates
    latitude, longitude = location.latlng
    if config.USE_ROUNDED_COORDS:
        latitude, longitude = map(lambda x: round(x, 1), [latitude, longitude])
    return Coordinates(latitude=latitude, longitude=longitude)


if __name__ == '__main__':
    print(get_coordinates())

# from dataclasses import dataclass

# 2)
# def get_gps_coordinates() -> dict[Literal['latitude'] | Literal['longitude'], float]
#     """Returns current coordinates using"""
#     return {'latitude' : 10.0, 'longitude' : 15.0}
# coordinates = get_gps_coordinates()
# print(coordinates['latitude'])

# 3) There is no real usage
# class Coordinates(TypedDict):
#     latitude: float
#     longitude: float
#
#
# def get_gps_coordinates() -> Coordinates:
#     """Returns current coordinates using"""
#     return Coordinates(**{'latitude': 10.0, 'longitude': 15.0})
#
#
# coordinates = get_gps_coordinates()
# print(coordinates['latitude'])


# @dataclass
# class Coordinates:
#     latitude: float
#     longitude: float
#
#
# def get_gps_coordinates() -> Coordinates:
#     """Returns current coordinates using"""
#     return Coordinates(latitude=10.0, longitude=15.0)
#
#
# coordinates = get_gps_coordinates()
# print(coordinates.latitude)
