# Animated Weather App

A beautiful, animated weather application built with Flask and modern web technologies.

## Features

✨ **Beautiful Animations**
- Smooth page transitions and loading animations
- Weather-responsive background effects (sunny, cloudy, rainy, snowy)
- Floating weather icons and detail card animations

🌍 **Real Weather Data**
- Current weather information
- 5-day forecast
- Comprehensive weather details (temperature, humidity, wind speed, pressure)

📱 **Responsive Design**
- Works perfectly on desktop, tablet, and mobile devices
- Clean and intuitive user interface

## Installation

1. Navigate to the project directory:
   ```bash
   cd weather-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

3. Enter a city name and click "Search" to see the animated weather display!

## API Endpoints

- `GET /` - Main app page
- `GET /api/weather?city=<city_name>` - Get current weather
- `GET /api/forecast?city=<city_name>` - Get 5-day forecast

## Project Structure

```
weather-app/
├── app.py                 # Flask application
├── weather_service.py     # Weather API service
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main HTML template
└── static/
    ├── style.css         # Styles and animations
    └── script.js         # Frontend JavaScript
```

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **API**: OpenWeatherMap API
- **Animations**: CSS3 keyframe animations

## Weather Icons

Different weather conditions display unique animated backgrounds:
- ☀️ Sunny - Bright gradient with brightness animations
- ⛅ Cloudy - Soft gradient with opacity animations
- 🌧️ Rainy - Dark gradient with brightness dynamics
- ❄️ Snowy - Cool gradient with subtle blur effects

## License

This project is licensed under the MIT License.
