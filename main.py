from display import WeatherDisplay
from weather_service import WeatherService
from storage import Storage

def main():
    service = WeatherService()
    display = WeatherDisplay()
    storage = Storage()
    
    while True:
        print("\n" + "="*50)
        print("🌤️  WEATHER APP")
        print("="*50)
        print("1. Check weather for a city")
        print("2. View favorite cities")
        print("3. Add city to favorites")
        print("4. Remove city from favorites")
        print("5. Exit")
        print("="*50)
        
        choice = input("\nSelect an option (1-5): ").strip()
        
        if choice == "1":
            city = input("Enter city name: ").strip()
            if city:
                data = service.get_weather(city)
                if data:
                    display.show_weather(data)
                else:
                    print("❌ Could not fetch weather data. Please try again.")
        
        elif choice == "2":
            favorites = storage.get_favorites()
            if not favorites:
                print("\n📝 No favorite cities yet!")
            else:
                print("\n⭐ Your Favorite Cities:")
                for idx, city in enumerate(favorites, 1):
                    print(f"{idx}. {city}")
                
                city_choice = input("\nEnter number to check weather (or press Enter to go back): ").strip()
                if city_choice.isdigit():
                    idx = int(city_choice) - 1
                    if 0 <= idx < len(favorites):
                        data = service.get_weather(favorites[idx])
                        if data:
                            display.show_weather(data)
        
        elif choice == "3":
            city = input("Enter city name to add to favorites: ").strip()
            if city:
                storage.add_favorite(city)
                print(f"✅ Added {city} to favorites!")
        
        elif choice == "4":
            favorites = storage.get_favorites()
            if not favorites:
                print("\n📝 No favorite cities to remove!")
            else:
                print("\n⭐ Your Favorite Cities:")
                for idx, city in enumerate(favorites, 1):
                    print(f"{idx}. {city}")
                
                city_choice = input("\nEnter number to remove (or press Enter to cancel): ").strip()
                if city_choice.isdigit():
                    idx = int(city_choice) - 1
                    if 0 <= idx < len(favorites):
                        removed = storage.remove_favorite(idx)
                        print(f"✅ Removed {removed} from favorites!")
        
        elif choice == "5":
            print("\n👋 Thanks for using Weather App!")
            break
        
        else:
            print("❌ Invalid option. Please try again.")

if _name_ == "_main_":
    main()