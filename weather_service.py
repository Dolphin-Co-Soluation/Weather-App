import requests
import random

class WeatherService:
    """Fetches weather data (using mock data for demo)"""
    
    def get_weather(self, city):
        """Get current weather and 3-day forecast"""
        # In production, use: api.openweathermap.org or weatherapi.com
        # For demo, generating realistic mock data
        
        try:
            # Mock current weather
            temp = random.randint(15, 35)
            conditions = ["Sunny", "Cloudy", "Rainy", "Partly Cloudy", "Clear"]
            condition = random.choice(conditions)
            humidity = random.randint(40, 90)
            
            # Generate 3-day forecast
            forecast = []
            for day in range(1, 4):
                day_temp = temp + random.randint(-5, 5)
                day_condition = random.choice(conditions)
                forecast.append({
                    'day': f"Day {day}",
                    'temp': day_temp,
                    'condition': day_condition
                })
            
            # Check for alerts
            alerts = []
            if temp > 32:
                alerts.append(("Heat Alert", "Temperature exceeds 32°C"))
            if condition == "Rainy":
                alerts.append(("Rain Alert", "Rainy conditions expected"))
            if humidity > 80:
                alerts.append(("Humidity Alert", "High humidity levels"))
            
            return {
                'city': city.title(),
                'current': {
                    'temp': temp,
                    'condition': condition,
                    'humidity': humidity
                },
                'forecast': forecast,
                'alerts': alerts
            }
        
        except Exception as e:
            print(f"Error fetching weather: {e}")
            return None
