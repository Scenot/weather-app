import requests
import sqlite3
import datetime

class WeatherApp:
    def __init__(self, api_key, db_filename):
        self.api_key = api_key
        self.conn = sqlite3.connect(db_filename)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS search_history (
            id INTEGER PRIMARY KEY, city TEXT, temperature REAL, description TEXT, timestamp TEXT
            )""")
        self.conn.commit()

    def fetch_weather(self, city):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"

        try:
            response = requests.get(url, verify=False)

            if response.status_code == 200:
                data = response.json()
                temperature = data["main"]["temp"]
                description = data["weather"][0]["description"]
                city_name = data["name"]
                return city_name, description, temperature
            elif response.status_code == 404:
                print(f"City '{city}' not found!")
                return None
            else:
                print(f"Error '{response.status_code}'!")
                return None
        except requests.exceptions.ConnectionError:
            print("Connection error! Check your internet connection!")
            return None

    def save_history(self, city, temperature, description):
        now = datetime.datetime.now()
        formatted = now.strftime("%Y-%m-%d %H:%M")

        self.cursor.execute("INSERT INTO search_history(city, temperature, description, timestamp) VALUES (?, ?, ?, ?)", (city, temperature, description, formatted))
        self.conn.commit()

    def show_history(self):
        self.cursor.execute("SELECT * FROM search_history ORDER BY id")
        rows = self.cursor.fetchall()

        if rows:
            print("\nRecent searches:")
            for row in rows:
                print(f"{row[4]} - {row[1]}: {row[2]}°C, {row[3]}")
        else:
            print("No history yet.")

    def run(self):
        while True:
            print("\n--- Weather App ---\n")
            print("1. Check weather.")
            print("2. Show history.")
            print("3. Quit")

            answer = input("Choose number: ")

            if answer == "1":
                city = input("Name your city: ")
                result = self.fetch_weather(city)

                if result:
                    name, desc, temp = result
                    print(f"\nWeather in {name}:")
                    print(f"Temperature: {temp}°C")
                    print(f"Conditions: {desc}")
                    self.save_history(name, temp, desc)

            elif answer == "2":
                self.show_history()

            elif answer == "3":
                print("Bye!")
                break

            else:
                print("Invalid!")

    def close(self):
        self.conn.close()

from config import API_KEY

if __name__ == "__main__":
    app = WeatherApp("API_KEY", "weather.db")
    app.run()
    app.close()