from flask import Flask, render_template, jsonify, request
from weather_service import WeatherService
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

# Initialize weather service
API_KEY = "01b576bd75df983f7d4b0ed7db61dff5"
weather_service = WeatherService(API_KEY)

@app.route('/')
def index():
    """Render the main weather app page"""
    return render_template('index.html')

@app.route('/api/weather', methods=['GET'])
def get_weather():
    """API endpoint to fetch weather data"""
    city = request.args.get('city', '').strip()
    
    if not city:
        return jsonify({'error': 'City name is required'}), 400
    
    try:
        weather = weather_service.get_current_weather(city)
        return jsonify(weather)
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except ConnectionError as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'}), 500

@app.route('/api/forecast', methods=['GET'])
def get_forecast():
    """API endpoint to fetch weather forecast"""
    city = request.args.get('city', '').strip()
    
    if not city:
        return jsonify({'error': 'City name is required'}), 400
    
    try:
        forecast = weather_service.get_forecast(city)
        return jsonify(forecast)
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': 'Failed to fetch forecast'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
