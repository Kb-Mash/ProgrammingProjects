# Weather App (API Project)

A simple Python app that fetches real-time weather data from an external API and displays it in a user-friendly format.

## 🌤️ Overview

This weather app lets users enter a city name and retrieves live weather information (temperature, conditions, humidity, etc.) using a public weather API (e.g., OpenWeatherMap). It helps practice API integration, HTTP requests, and JSON parsing.

## 🚀 Features

- City search input
- Current temperature display
- Weather condition description (clear, rain, clouds, etc.)
- Additional fields (optional enhancements): humidity, wind speed, feels like
- Error handling for invalid city names or network failures

## 📦 Installation

1. Clone the repo:

```bash
git clone https://github.com/Kb-Mash/ProgrammingProjects.git
cd ProgrammingProjects/weatherApp
```

2. Get an API key from [OpenWeatherMap](https://openweathermap.org/api) (free tier available).

3. Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

4. Set your API key as an environment variable:

```bash
export OPENWEATHER_API_KEY="your_api_key_here"
```

Or edit `weather_app.py` and replace `'your_api_key_here'` with your key.

## ▶️ Usage

```bash
python weather_app.py
```

Then enter a valid city name when prompted.

## 🧠 Implementation notes

- Use `requests` for GET calls to the weather API
- Parse JSON response for desired fields
- Handle non-200 responses gracefully
- Keep keys/config separate from code (environment variables or config file)

## 💡 Enhancements

- Add cache to minimize repeated API calls
- Support multiple cities at once
- CLI options with `argparse` for units (`metric`/`imperial`)
- GUI using Tkinter or web UI using Flask

## 🧩 Skills Learned

- Consuming web APIs
- HTTP request/response lifecycle
- JSON parsing and data mapping
- User input validation

## 📝 License

This project is open source and available under the [MIT License](LICENSE).