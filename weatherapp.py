import requests
import tkinter as tk
from tkinter import messagebox

class WeatherApp:
    def __init__(self, root, api_key):
        self.root = root
        self.api_key = api_key
        self.root.title("Weather Fetcher")
        
        # Setup the UI components
        self.setup_ui()

    def setup_ui(self):
        # City input
        self.city_label = tk.Label(self.root, text="Enter City Name:")
        self.city_label.pack(pady=10)
        
        self.city_entry = tk.Entry(self.root, width=40)
        self.city_entry.pack(pady=5)
        
        # Fetch weather button
        self.fetch_button = tk.Button(self.root, text="Fetch Weather", command=self.fetch_weather)
        self.fetch_button.pack(pady=10)
        
        # Result area
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=20)
        
    def fetch_weather(self):
        city = self.city_entry.get()
        if not city:
            messagebox.showerror("Input Error", "Please enter a city name")
            return
        
        weather_data = self.get_weather_by_city(city)
        if weather_data:
            self.display_weather(weather_data)
        else:
            messagebox.showerror("Error", "Unable to fetch weather data")

    def get_weather_by_city(self, city):
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = f"{base_url}q={city}&appid={self.api_key}&units=metric"
        try:
            response = requests.get(complete_url)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Request failed: {e}")
            return None
    
    def display_weather(self, data):
        main = data['main']
        weather = data['weather'][0]
        wind = data['wind']
        
        weather_info = (
            f"City: {data['name']}\n"
            f"Temperature: {main['temp']}°C\n"
            f"Humidity: {main['humidity']}%\n"
            f"Pressure: {main['pressure']} hPa\n"
            f"Weather: {weather['description'].capitalize()}\n"
            f"Wind Speed: {wind['speed']} m/s\n"
            f"Wind Direction: {wind['deg']}°"
        )
        
        self.result_label.config(text=weather_info)

if __name__ == "__main__":
    root = tk.Tk()
    
    # Replace with your actual OpenWeatherMap API key
    api_key = "YOUR_API_KEY"
    
    app = WeatherApp(root, api_key)
    root.mainloop()




