import matplotlib.pyplot as plt

class WeatherDisplay:
    """Handles all display and visualization"""
    
    def show_weather(self, data):
        """Display current weather, forecast, and chart"""
        print("\n" + "="*50)
        print(f"📍 {data['city']}")
        print("="*50)
        
        # Current weather
        current = data['current']
        print(f"\n🌡️  Current Weather:")
        print(f"   Temperature: {current['temp']}°C")
        print(f"   Condition: {current['condition']}")
        print(f"   Humidity: {current['humidity']}%")
        
        # Alerts
        if data['alerts']:
            print(f"\n⚠️  ALERTS:")
            for alert_type, alert_msg in data['alerts']:
                # Red text for heat alerts
                if "Heat" in alert_type:
                    print(f"   \033[91m🔥 {alert_type}: {alert_msg}\033[0m")
                else:
                    print(f"   ⚠️  {alert_type}: {alert_msg}")
        
        # Forecast
        print(f"\n📅 3-Day Forecast:")
        for day_data in data['forecast']:
            print(f"   {day_data['day']}: {day_data['temp']}°C - {day_data['condition']}")
        
        # Show chart
        self.show_temperature_chart(data)
        print("="*50)
    
    def show_temperature_chart(self, data):
        """Draw temperature chart for forecast"""
        days = ['Today'] + [f['day'] for f in data['forecast']]
        temps = [data['current']['temp']] + [f['temp'] for f in data['forecast']]
        
        plt.figure(figsize=(10, 5))
        plt.plot(days, temps, marker='o', linewidth=2, markersize=8, color='#FF6B6B')
        plt.fill_between(range(len(days)), temps, alpha=0.3, color='#FF6B6B')
        plt.xlabel('Day', fontsize=12)
        plt.ylabel('Temperature (°C)', fontsize=12)
        plt.title(f'Temperature Trend - {data["city"]}', fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
