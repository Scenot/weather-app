# Weather CLI App

A command-line weather application built with Python.

## Features

- Check current weather for any city
- Live data from OpenWeatherMap API
- Shows temperature and weather conditions
- Saves search history to SQLite
- View past searches

## Requirements

- Python 3.8+
- `requests` library
- An OpenWeatherMap API key (free at openweathermap.org)

## Setup

1. Install the required library:

    pip install requests

2. Create a file called `config.py` in the project folder with your API key:

    API_KEY = "your_api_key_here"

3. Run the app:

    python weather_API.py

## How to Use

Choose from the menu:
1. Check weather — enter a city name
2. Show history — view past searches
3. Quit

## Project Structure

- `weather_API.py` — main application
- `config.py` — stores your API key (not committed to Git)
- `.gitignore` — excludes sensitive files from Git
- `test_weather_API.py` — automated tests

## What I Learned

- Object-oriented programming with classes
- Working with REST APIs and JSON data
- Error handling for network requests
- SQLite database integration
- Git and GitHub workflow