

import os
import sys

import requests
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class WeatherApp(QWidget):
    API_URL = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Weather App")
        self.setMinimumSize(560, 650)
        self.resize(700, 760)

        self.build_ui()
        self.apply_styles()

        self.get_weather_button.clicked.connect(self.get_weather)
        self.city_input.returnPressed.connect(self.get_weather)

    def build_ui(self):
        main = QVBoxLayout(self)
        main.setContentsMargins(26, 24, 26, 24)
        main.setSpacing(16)

        # Header
        title = QLabel("Weather App  ☀️")
        title.setObjectName("app_title")

        subtitle = QLabel("Weather updates for your city")
        subtitle.setObjectName("subtitle")

        main.addWidget(title)
        main.addWidget(subtitle)

        # City search
        search = QHBoxLayout()
        search.setSpacing(10)

        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Enter a city, e.g. Nairobi")
        self.city_input.setClearButtonEnabled(True)
        self.city_input.setObjectName("city_input")

        self.get_weather_button = QPushButton("Search")
        self.get_weather_button.setObjectName("search_button")
        self.get_weather_button.setCursor(Qt.PointingHandCursor)

        search.addWidget(self.city_input, 1)
        search.addWidget(self.get_weather_button)
        main.addLayout(search)

        # Main weather card
        weather_card = QFrame()
        weather_card.setObjectName("weather_card")

        weather_layout = QVBoxLayout(weather_card)
        weather_layout.setContentsMargins(20, 18, 20, 18)
        weather_layout.setSpacing(8)

        self.city_label = QLabel("Welcome!")
        self.city_label.setObjectName("city_label")
        self.city_label.setAlignment(Qt.AlignCenter)

        self.emoji_label = QLabel("🌤️")
        self.emoji_label.setObjectName("weather_icon")
        self.emoji_label.setAlignment(Qt.AlignCenter)

        self.temperature_label = QLabel("--°C")
        self.temperature_label.setObjectName("temperature_label")
        self.temperature_label.setAlignment(Qt.AlignCenter)

        self.description_label = QLabel("Search for a city to begin")
        self.description_label.setObjectName("description_label")
        self.description_label.setAlignment(Qt.AlignCenter)
        self.description_label.setWordWrap(True)

        self.updated_label = QLabel("Current weather")
        self.updated_label.setObjectName("updated_label")
        self.updated_label.setAlignment(Qt.AlignCenter)

        weather_layout.addWidget(self.city_label)
        weather_layout.addWidget(self.emoji_label)
        weather_layout.addWidget(self.temperature_label)
        weather_layout.addWidget(self.description_label)
        weather_layout.addWidget(self.updated_label)

        main.addWidget(weather_card)

        # Metrics heading
        heading = QLabel("Weather Details")
        heading.setObjectName("section_title")
        main.addWidget(heading)

        # Four metric cards
        grid = QGridLayout()
        grid.setSpacing(12)

        metrics = [
            ("feels_like", "🌡️", "Feels like", "--°C"),
            ("humidity", "💧", "Humidity", "--%"),
            ("wind", "💨", "Wind speed", "-- km/h"),
            ("pressure", "📊", "Pressure", "-- hPa"),
        ]

        self.metric_values = {}

        for index, (key, icon, name, initial) in enumerate(metrics):
            card, value_label = self.create_metric_card(
                icon, name, initial
            )
            self.metric_values[key] = value_label
            grid.addWidget(card, index // 2, index % 2)

        main.addLayout(grid)

        # Status and footer
        self.status_label = QLabel("Ready to search.")
        self.status_label.setObjectName("status_label")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setWordWrap(True)

        main.addWidget(self.status_label)

        footer = QLabel("Weather data powered by OpenWeatherMap")
        footer.setObjectName("footer")
        footer.setAlignment(Qt.AlignCenter)
        main.addWidget(footer)

    def create_metric_card(self, icon, name, initial_value):
        card = QFrame()
        card.setObjectName("metric_card")

        layout = QVBoxLayout(card)
        layout.setContentsMargins(15, 14, 15, 14)
        layout.setSpacing(8)

        heading = QHBoxLayout()
        heading.setSpacing(8)

        icon_label = QLabel(icon)
        icon_label.setObjectName("metric_icon")

        name_label = QLabel(name)
        name_label.setObjectName("metric_name")

        heading.addWidget(icon_label)
        heading.addWidget(name_label)
        heading.addStretch()

        value_label = QLabel(initial_value)
        value_label.setObjectName("metric_value")

        layout.addLayout(heading)
        layout.addWidget(value_label)

        return card, value_label

    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #edf5ff;
                color: #18365e;
                font-family: "Segoe UI", Arial, sans-serif;
            }

            QLabel#app_title {
                font-size: 30px;
                font-weight: bold;
                color: #1557a6;
            }

            QLabel#subtitle {
                font-size: 14px;
                color: #657d9a;
            }

            QLineEdit#city_input {
                background-color: white;
                border: 1px solid #c8dbf2;
                border-radius: 12px;
                padding: 12px;
                font-size: 15px;
                color: #18365e;
            }

            QLineEdit#city_input:focus {
                border: 2px solid #3182e8;
            }

            QPushButton#search_button {
                background-color: #1976d2;
                color: white;
                border: none;
                border-radius: 12px;
                padding: 12px 20px;
                font-size: 15px;
                font-weight: bold;
            }

            QPushButton#search_button:hover {
                background-color: #125eaa;
            }

            QPushButton#search_button:disabled {
                background-color: #8baed1;
            }

            QFrame#weather_card {
                background-color: #dceeff;
                border: 1px solid #b9d8fb;
                border-radius: 20px;
            }

            QLabel#city_label {
                font-size: 22px;
                font-weight: bold;
                color: #194c88;
            }

            QLabel#weather_icon {
                font-size: 62px;
                background: transparent;
            }

            QLabel#temperature_label {
                font-size: 52px;
                font-weight: bold;
                color: #104b91;
            }

            QLabel#description_label {
                font-size: 20px;
                font-weight: bold;
                color: #245b96;
            }

            QLabel#updated_label {
                font-size: 12px;
                color: #637b9b;
            }

            QLabel#section_title {
                font-size: 20px;
                font-weight: bold;
                color: #18365e;
            }

            QFrame#metric_card {
                background-color: white;
                border: 1px solid #d7e5f6;
                border-radius: 15px;
            }

            QLabel#metric_icon {
                font-size: 20px;
                background: transparent;
            }

            QLabel#metric_name {
                font-size: 13px;
                color: #71839d;
                background: transparent;
            }

            QLabel#metric_value {
                font-size: 21px;
                font-weight: bold;
                color: #194c88;
                background: transparent;
            }

            QLabel#status_label {
                font-size: 13px;
                color: #536e90;
            }

            QLabel#footer {
                font-size: 11px;
                color: #71839d;
            }
        """)

    def get_weather(self):
        city = self.city_input.text().strip()
        api_key = os.getenv("OPENWEATHER_API_KEY")

        if not city:
            self.display_error("Please enter a city name.")
            return

        if not api_key:
            self.display_error(
                "API key missing. Set OPENWEATHER_API_KEY "
                "in your VS Code PowerShell terminal."
            )
            return

        self.get_weather_button.setEnabled(False)
        self.get_weather_button.setText("Loading...")
        self.status_label.setText("Fetching weather data...")

        QApplication.setOverrideCursor(Qt.WaitCursor)

        try:
            response = requests.get(
                self.API_URL,
                params={
                    "q": city,
                    "appid": api_key,
                    "units": "metric",
                },
                timeout=10,
            )

            response.raise_for_status()
            data = response.json()

            current = data["main"]
            weather = data["weather"][0]
            wind = data.get("wind", {})

            temperature = current["temp"]
            feels_like = current["feels_like"]
            humidity = current["humidity"]
            pressure = current["pressure"]
            wind_kmh = wind.get("speed", 0) * 3.6

            self.city_label.setText(
                f"{data['name']}, {data['sys']['country']}"
            )
            self.temperature_label.setText(f"{temperature:.1f}°C")
            self.emoji_label.setText(
                self.get_weather_emoji(weather["id"])
            )
            self.description_label.setText(
                weather["description"].capitalize()
            )

            self.metric_values["feels_like"].setText(
                f"{feels_like:.1f}°C"
            )
            self.metric_values["humidity"].setText(f"{humidity}%")
            self.metric_values["wind"].setText(
                f"{wind_kmh:.1f} km/h"
            )
            self.metric_values["pressure"].setText(
                f"{pressure} hPa"
            )

            self.updated_label.setText("Current conditions")
            self.status_label.setText("Weather updated successfully.")

        except requests.exceptions.HTTPError:
            messages = {
                400: "Invalid request. Check the city name.",
                401: "Invalid API key or key not activated yet.",
                403: "Access denied by the weather service.",
                404: "City not found. Check the spelling.",
                429: "Too many requests. Try again later.",
                500: "Weather service error. Try again later.",
                502: "Weather service gateway error.",
                503: "Weather service is unavailable.",
                504: "Weather service timed out.",
            }

            self.display_error(
                messages.get(
                    response.status_code,
                    f"Request failed: HTTP {response.status_code}",
                )
            )

        except requests.exceptions.Timeout:
            self.display_error("Request timed out. Try again.")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection error. Check your internet.")

        except (
            requests.exceptions.RequestException,
            KeyError,
            IndexError,
            TypeError,
            ValueError,
        ):
            self.display_error("Could not read weather data.")

        finally:
            QApplication.restoreOverrideCursor()
            self.get_weather_button.setEnabled(True)
            self.get_weather_button.setText("Search")

    def display_error(self, message):
        self.status_label.setText(message)

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌦️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 781:
            return "🌫️"
        elif weather_id == 800:
            return "☀️"
        elif weather_id == 801:
            return "🌤️"
        elif 802 <= weather_id <= 804:
            return "☁️"
        return "🌡️"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec())
