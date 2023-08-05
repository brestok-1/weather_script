from environs import Env

env = Env()
env.read_env()

USE_ROUNDED_COORDS = False
OPENWEATHER_API = env('API_KEY')

OPENWEATHER_URL = (
        "https://api.openweathermap.org/data/2.5/weather?"
        "lat={latitude}&lon={longitude}&"
        "appid=" + OPENWEATHER_API + "&lang=ru&"
                                     "units=metric"
)
