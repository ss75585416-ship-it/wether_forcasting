# wether_forcasting
A Python-based weather application that integrates the Open-Meteo Geocoding and Weather APIs to retrieve geographical coordinates and real-time weather information using HTTP requests.
# Python Weather API 🌦️

## Overview
A beginner-friendly Python project that demonstrates REST API integration using the Requests library and Open-Meteo APIs.

The application accepts a city name, retrieves its geographical coordinates through the Geocoding API, and uses those coordinates to fetch current weather information.

## Features
- City-based geographical search.
- Automatic latitude and longitude retrieval.
- Current temperature retrieval.
- Relative humidity retrieval.
- JSON response handling.
- HTTP GET requests using Python Requests.

## Technologies Used
- Python
- Requests Library
- REST APIs
- JSON
- Open-Meteo API

## APIs Integrated

**1. Geocoding API**

Converts a city name into geographical coordinates.

**2. Weather Forecast API**

Uses latitude and longitude to retrieve current weather information.

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Install dependencies:

```bash
pip install requests
```

Run the application:

```bash
python main.py
```

## Learning Outcomes

- Understanding HTTP GET requests.
- Working with API endpoints and query parameters.
- Understanding JSON responses.
- Extracting nested dictionary and list values.
- Integrating multiple APIs into a single Python application.

## Data Source

Open-Meteo: https://open-meteo.com/

## Future Improvements
- Dynamic city input.
- Weather condition descriptions.
- Error handling for invalid locations.
- Hourly and daily weather forecasts.
- User-friendly interface.

## Author
Shashank P
AI & ML Engineering Student
