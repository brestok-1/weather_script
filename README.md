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

I wrote a python bot using aiogram. I used two databases: Postgresql for storing user data, books and bookmarks, and
Redis for caching data and optimizing work. The bot takes data about books via API from
a [third-party service](https://github.com/brestok-1/drf-tg-data) and stores
them in the database. With the help of the Aiocron library, the database is updated every hour. I also connected an
alembic to initialize the database and create migrations

## Project setup

***Method 2: Via virtual environment***

1. Create and activate a python virtual environment
2. In the terminal, enter the following command:

```
pip3 install -r requirements.txt
```

3. Run the file weather

## <div align="center">Thank you for taking the time to review my project. Enjoy reading!👋</div>