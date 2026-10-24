
# 🌦️ Weather App — Python Desktop Application

**Technologies:** Python, PyQt5, Requests, OpenWeatherMap API

## 📌 Project Overview

Developed a Python desktop weather application that retrieves and displays current weather conditions for user-selected cities through an interactive graphical interface.

The project demonstrates practical skills in Python development, REST API integration, desktop GUI design, error handling, and secure API-key configuration.

## ✨ Key Features

- **Weather API Integration:** Retrieves current weather information using the OpenWeatherMap API.
- **Weather Details:** Displays temperature in Celsius, feels-like temperature, humidity, wind speed in km/h, atmospheric pressure in hPa, and weather descriptions.
- **Graphical User Interface:** Provides an interactive desktop interface built with PyQt5, custom styling, and organized weather information.
- **City Search:** Allows users to search for weather conditions by clicking the search button or pressing Enter.
- **Error Handling:** Displays user-friendly messages for invalid city names, missing API configuration, HTTP errors, timeouts, and network connection failures.
- **API-Key Security:** Reads the API key from the `OPENWEATHER_API_KEY` environment variable instead of hardcoding the credential in the source code.

## 🖥️ Screenshots

Add a screenshot of the running application here to demonstrate its interface.

To display an image hosted in your repository, upload a screenshot to a folder such as `screenshots/` and use:

```markdown
![Weather App Interface](screenshots/weather-app.png)
```

Replace the image path with the actual filename and location of your screenshot.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application logic |
| PyQt5 | Desktop graphical user interface |
| Requests | HTTP requests and API communication |
| OpenWeatherMap API | Current weather data |
| Environment Variables | API-key configuration |

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_WEATHER_APP_REPOSITORY_URL
cd YOUR_REPOSITORY_FOLDER
```

Replace the placeholders with your actual GitHub repository URL and folder name.

### 2. Create a Virtual Environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```powershell
python -m pip install PyQt5 requests
```

### 4. Configure the OpenWeatherMap API Key

Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api).

Set the environment variable in Windows PowerShell:

```powershell
$env:OPENWEATHER_API_KEY = "your_actual_api_key"
```

Replace the placeholder with your actual API key. This setting applies to the current terminal session.

### 5. Run the Application

Assuming the Python script is named `weather_app.py`:

```powershell
python weather_app.py
```

If your script has a different filename, use the correct filename.

## 🔐 Security Considerations

- Do not hardcode API credentials in source code.
- Do not commit actual API keys to GitHub.
- Keep local environment files and virtual environments out of version control.
- Use the `OPENWEATHER_API_KEY` environment variable to configure the application.

## 🎯 Skills Demonstrated

- Python programming and desktop application development
- REST API integration and JSON response handling
- PyQt5 GUI development and interface styling
- Environment-variable configuration and credential management
- Exception handling and network troubleshooting
- User input validation and error reporting
- GitHub repository management and technical documentation

## 🚀 Potential Future Enhancements

- Add a multi-day weather forecast.
- Support Celsius and Fahrenheit conversion.
- Add saved cities and recent search history.
- Improve automated testing and API-response validation.
- Package the application as a standalone Windows executable.

## 👨‍💻 Author

**Kephas Abonyo**

- **GitHub Profile:** [KE2541](https://github.com/KE2541)
- **Project Type:** Personal learning and portfolio project.

## ⚠️ Disclaimer

This application is intended for educational and portfolio purposes. Weather information depends on the availability and accuracy of the third-party API and is subject to its usage limits and terms.
