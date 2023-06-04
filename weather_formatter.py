from weather_api_service import Weather


def format_weather(weather: Weather) -> str:
    """Formats weather data in string"""
    return (f"{weather.city}, the temperature is {weather.temperature} °C, "
            f"{weather.weather_type.value}\n"
            f"Sunrise: {weather.sunrise.strftime('%H:%M')}\n"
            f"Sunset: {weather.sunset.strftime('%H:%M')}\n")


if __name__ == '__main__':
    from datetime import datetime
    from weather_api_service import WeatherType

    print(format_weather(Weather(
        temperature=25,
        weather_type=WeatherType.RAIN,
        sunrise=datetime.fromisoformat("2023-05-03 04:00:00"),
        sunset=datetime.fromisoformat("2023-05-03 20:25:00"),
        city='Brest'
    )))
