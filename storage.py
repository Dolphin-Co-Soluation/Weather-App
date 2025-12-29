import json
import os

class Storage:
    """Handles saving and loading favorite cities"""
    
    def _init_(self, filename='favorites.json'):
        self.filename = filename
    
    def get_favorites(self):
        """Load favorite cities from file"""
        if not os.path.exists(self.filename):
            return []
        
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except:
            return []
    
    def add_favorite(self, city):
        """Add a city to favorites"""
        favorites = self.get_favorites()
        city_title = city.title()
        
        if city_title not in favorites:
            favorites.append(city_title)
            self._save_favorites(favorites)
    
    def remove_favorite(self, index):
        """Remove a city from favorites by index"""
        favorites = self.get_favorites()
        if 0 <= index < len(favorites):
            removed = favorites.pop(index)
            self._save_favorites(favorites)
            return removed
        return None
    
    def _save_favorites(self, favorites):
        """Save favorites to file"""
        with open(self.filename, 'w') as f:
            json.dump(favorites, f, indent=2)
