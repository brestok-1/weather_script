# <div align="center">Weather script ⛅</div>

<div align="center">
<img src="assets/main-photo.jpg" align="center" style="width: 100%; height: 40%" />
</div>

<br/>

I watched a video on how to improve the quality of my code. After watching it, I tried to put the acquired skills into
practice. I wrote a script that shows it instantly, defining it globally, so I can call it from any directory. I tried
to document the code as much as possible, apply typing, break functions into auxiliary functions and follow the rule
of good code.

## Description

<div align="center">
<img src="assets/output.png" align="center" style="width: 100%; height: 40%" />
</div>
<br/>

My weather script, by entering the weather command, instantly displays the current temperature, the presence of
precipitation, the time of sunrise and sunset according to your geolocation. In addition, it saves the data in a txt or
json file.

## Technologies

***Language***

![Python](https://img.shields.io/badge/-Python-1C1C1C?&style=for-the-badge)

***Libraries***

![Requests](https://img.shields.io/badge/-Requests-1C1C1C?&style=for-the-badge)
![geocoder](https://img.shields.io/badge/-geocoder-1C1C1C?&style=for-the-badge)
![mypy](https://img.shields.io/badge/-mypy-1C1C1C?&style=for-the-badge)

***Other***

![Openweather](https://img.shields.io/badge/-Openweather-1C1C1C?&style=for-the-badge)

The primary task was to obtain the longitude and latitude of the user, for which I used the geocoder library that
retrieves coordinates based on IP. Next, I passed the obtained data to an API request to the OpenWeather service, which
returns weather information in JSON format. Then, I parsed the JSON string and extracted the temperature, sunrise and
sunset times, precipitation, and displayed the obtained data in the console. Finally, I decided to add functions for
saving the results in TXT and JSON formats.

## Project setup

***Via virtual environment***

1. Create and activate a python virtual environment
2. In the terminal, enter the following command:

```
pip3 install -r requirements.txt
```

3. Create a .env file and paste the data from the .env.example file into it
4. Sign up to OpenWeather service and add your API key into .env file
5. Run the "weather" file

## <div align="center">Sunny weather for you!👋</div>