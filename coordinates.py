from typing import NamedTuple, Sequence
import geocoder  # type: ignore

import config
from exceptions import CantGetCoordinates


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_coordinates() -> Coordinates:
    """Returns current coordinates """
    coordinates = _get_geocoder_coordinates()
    return _round_coordinates(coordinates)


def _get_geocoder_coordinates() -> Coordinates:
    geocoder_output = _get_geocoder_output()
    coordinates = _parse_coordinate(geocoder_output)
    return coordinates


def _get_geocoder_output() -> Sequence[float]:
    location = geocoder.ip('me')
    if not location.status_code == 200:
        raise CantGetCoordinates
    return location.latlng


def _parse_coordinate(output: Sequence[float]) -> Coordinates:
    try:
        latitude, longitude = output
    except ValueError:
        raise CantGetCoordinates
    return Coordinates(latitude=latitude, longitude=longitude)


def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    if not config.USE_ROUNDED_COORDS:
        return coordinates
    return Coordinates(*map(lambda x: round(x, 1), [coordinates.latitude, coordinates.longitude]))


if __name__ == '__main__':
    print(get_coordinates())

