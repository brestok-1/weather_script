from typing import NamedTuple


# from dataclasses import dataclass


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_coordinates() -> Coordinates:  # -> tuple[float, float]:  Defines what type of data the function should return
    """Returns current coordinates """
    return Coordinates(latitude=0.0, longitude=0.0)


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
