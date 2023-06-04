USE_ROUNDED_COORDS = False
OPENWEATHER_API = '909c7b331b35205c8a4b26780af01e47'

OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + OPENWEATHER_API + "&lang=ru&"
    "units=metric"
)

