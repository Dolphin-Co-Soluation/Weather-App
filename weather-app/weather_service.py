import requests
import json
import os
from datetime import datetime

class WeatherService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5"
        self.cache_file = "weather_cache.json"
    
    def get_current_weather(self, city):
        """Fetch current weather for a city"""
        try:
            url = f"{self.base_url}/weather"
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Calculate local time based on timezone
            timezone_offset = data['timezone']  # Offset in seconds
            utc_time = datetime.utcnow()
            local_time = datetime.utcfromtimestamp(data['dt'] + timezone_offset)
            
            weather_data = {
                'city': data['name'],
                'country': data['sys']['country'],
                'temperature': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'humidity': data['main']['humidity'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
                'wind_speed': data['wind']['speed'],
                'timezone': timezone_offset,
                'local_time': local_time.strftime('%I:%M:%S %p'),
                'local_time_short': local_time.strftime('%I:%M %p'),
                'timestamp': datetime.now().isoformat()
            }
            
            return weather_data
            
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                raise ValueError(f"City '{city}' not found. Please check the spelling.")
            else:
                raise ConnectionError(f"Failed to fetch weather data: {str(e)}")
        except requests.exceptions.ConnectionError:
            raise ConnectionError("No internet connection. Please check your network.")
        except requests.exceptions.Timeout:
            raise ConnectionError("Request timed out. Please try again.")
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")
    
    def get_forecast(self, city):
        """Fetch 3-day forecast for a city"""
        try:
            url = f"{self.base_url}/forecast"
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric',
                'cnt': 24  # 3 days (8 readings per day)
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            forecast_data = []
            for item in data['list'][::8]:  # Get one reading per day
                forecast_data.append({
                    'date': item['dt_txt'].split()[0],
                    'temperature': item['main']['temp'],
                    'description': item['weather'][0]['description'],
                    'icon': item['weather'][0]['icon'],
                    'humidity': item['main']['humidity']
                })
            
            return forecast_data[:3]  # Ensure only 3 days
            
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                raise ValueError(f"City '{city}' not found. Please check the spelling.")
            else:
                raise ConnectionError(f"Failed to fetch forecast data: {str(e)}")
        except requests.exceptions.ConnectionError:
            raise ConnectionError("No internet connection. Please check your network.")
        except requests.exceptions.Timeout:
            raise ConnectionError("Request timed out. Please try again.")
        except Exception as e:
            raise Exception(f"An error occurred: {str(e)}")
    
    def check_heat_alert(self, temperature):
        """Check if temperature exceeds 35°C"""
        return temperature > 35
    
    def save_to_cache(self, city, current_weather, forecast):
        """Save weather data to a JSON file"""
        try:
            cache_data = {
                'city': city,
                'current_weather': current_weather,
                'forecast': forecast,
                'heat_alert': self.check_heat_alert(current_weather['temperature']),
                'cached_at': datetime.now().isoformat()
            }
            
            with open(self.cache_file, 'w') as f:
                json.dump(cache_data, f, indent=4)
            
            return True
        except Exception as e:
            print(f"Failed to save cache: {str(e)}")
            return False
    
    def load_from_cache(self):
        """Load weather data from cache file"""
        try:
            if os.path.exists(self.cache_file):
                with open(self.cache_file, 'r') as f:
                    return json.load(f)
            return None
        except Exception as e:
            print(f"Failed to load cache: {str(e)}")
            return None
    
    def get_weather_data(self, city):
        """Main method to get weather data with caching"""
        try:
            current = self.get_current_weather(city)
            forecast = self.get_forecast(city)
            
            heat_alert = self.check_heat_alert(current['temperature'])
            
            self.save_to_cache(city, current, forecast)
            
            return {
                'current': current,
                'forecast': forecast,
                'heat_alert': heat_alert
            }
        except Exception as e:
            raise e