from weather_service import WeatherService

def display_current_weather(weather):
    """Display current weather information"""
    print("\n" + "="*50)
    print(f"📍 Current Weather in {weather['city']}, {weather['country']}")
    print("="*50)
    print(f"🌡️  Temperature: {weather['temperature']}°C")
    print(f"🤔 Feels Like: {weather['feels_like']}°C")
    print(f"☁️  Conditions: {weather['description'].title()}")
    print(f"💧 Humidity: {weather['humidity']}%")
    print(f"💨 Wind Speed: {weather['wind_speed']} m/s")
    print("="*50)

def display_forecast(forecast):
    """Display 3-day forecast"""
    print("\n📅 3-Day Forecast:")
    print("-"*50)
    for day in forecast:
        print(f"\n📆 {day['date']}")
        print(f"   🌡️  {day['temperature']}°C")
        print(f"   ☁️  {day['description'].title()}")
        print(f"   💧 {day['humidity']}%")
    print("-"*50)

def display_heat_alert():
    """Display heat alert warning"""
    print("\n" + "🔥"*25)
    print("⚠️  HEAT ALERT! ⚠️")
    print("Temperature exceeds 35°C!")
    print("Stay hydrated and avoid prolonged sun exposure.")
    print("🔥"*25 + "\n")

def main():
    API_KEY = "01b576bd75df983f7d4b0ed7db61dff5"
    
    weather_service = WeatherService(API_KEY)
    
    print("🌤️  Welcome to the Weather App!")
    print("-"*50)
    
    while True:
        city = input("\nEnter city name (or 'quit' to exit): ").strip()
        
        if city.lower() == 'quit':
            print("👋 Goodbye!")
            break
        
        if not city:
            print("⚠️  Please enter a valid city name.")
            continue
        
        try:
            print(f"\n🔍 Fetching weather data for {city}...")
            
            data = weather_service.get_weather_data(city)
            
            display_current_weather(data['current'])
            
            if data['heat_alert']:
                display_heat_alert()
            
            display_forecast(data['forecast'])
            
            print("\n✅ Data saved to weather_cache.json")
            
        except ValueError as e:
            print(f"❌ {str(e)}")
        except ConnectionError as e:
            print(f"❌ {str(e)}")
        except Exception as e:
            print(f"❌ An error occurred: {str(e)}")

if __name__ == "__main__":
    main()