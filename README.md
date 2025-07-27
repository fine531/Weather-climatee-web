# Climatee Weather 🌤️

**🌐 Live Demo: [https://climatee-weather.onrender.com](https://climatee-weather.onrender.com)**

A simple weather web application built with Django that shows current weather and forecasts for any city. I created this project to learn Django and API integration.

https://roadmap.sh/projects/weather-app

## ✨ Features

- 🌍 **Auto Location Detection** - Get weather for your current location instantly
- 🔍 **City Search** - Search weather for any city worldwide  
- 📊 **Current Weather** - Temperature, humidity, wind speed, and conditions
- ⏰ **24-Hour Forecast** - Detailed hourly predictions
- 📱 **Mobile Responsive** - Works perfectly on all devices
- 🚀 **Live Deployment** - Hosted on Railway cloud platform

## 📱 Screenshots

### 🏠 Homepage - Clean & Professional
![Desktop Homepage](./images/desktop-home.png)
*Beautiful landing page with "Welcome to Climatee!" message and intuitive location/search options*

### 🌤️ Live Weather Results - Karimnagar, IN
![Weather Details](./images/weather-display.png)
*Complete weather dashboard showing current conditions (24°C, Overcast Clouds) with detailed metrics (wind speed, humidity, rain) and comprehensive 24-hour forecast with 8 time periods*

### ✨ Key Features Demonstrated
- **Clean UI Design**: Professional gradient design with clear typography
- **Real Weather Data**: Live data from OpenWeather API showing actual conditions
- **Detailed Metrics**: Wind speed (8 m/s), Humidity (91%), Rain information
- **24-Hour Forecast**: 8 forecast cards with time, temperature, and weather icons
- **Responsive Layout**: Beautiful card-based layout that works on all devices

> **🚀 Live Demo**: Test all features yourself at [climatee-production.up.railway.app](https://climatee-production.up.railway.app)

## Tech Stack

- **Django 5.2.4** - Python web framework
- **Bootstrap 5** - For responsive design
- **OpenWeather API** - Weather data source
- **SQLite** - Database (default Django)
- **JavaScript** - For location detection

## How to run it

### Prerequisites
- Python 3.8+
- Internet connection (for weather API)

### Setup
1. Clone this repo
```bash
git clone <your-repo-url>
cd climatee
```

2. Create virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux  
source venv/bin/activate
```

3. Install requirements
```bash
pip install -r requirements.txt
```

4. Get API key
- Sign up at [OpenWeather](https://openweathermap.org/api)
- Get your free API key
- Create `.env` file in root folder:
```
OPENWEATHER_API_KEY=your_api_key_here
SECRET_KEY=your_secret_key
DEBUG=True
```

5. Setup database
```bash
python manage.py migrate
```

6. Run the server
```bash
python manage.py runserver
```

Visit `http://localhost:8000` to see the app!

## Features

### Current Weather
- Temperature in Celsius
- Weather description (sunny, rainy, etc.)
- Wind speed and humidity
- Location and country

### 24-Hour Forecast
- 8 time periods (every 3 hours)
- Temperature and conditions for each period
- Easy to read time format

### User Experience
- **Auto Location**: Click "Detect My Location" to get local weather
- **Search**: Type any city name to get weather
- **Mobile Friendly**: Works great on phones and tablets
- **Error Handling**: Shows helpful messages if something goes wrong

## API Integration

The app uses OpenWeather API endpoints:
- Current weather: `/data/2.5/weather`
- 5-day forecast: `/data/2.5/forecast` (we use first 24 hours)

## Project Structure

```
climatee/
├── config/          # Django project settings
├── weather/         # Main weather app
│   ├── templates/   # HTML files
│   ├── static/      # CSS, JS, images
│   ├── views.py     # Request handling
│   └── utils.py     # Weather API functions
├── manage.py        # Django commands
└── requirements.txt # Python packages
```

## Deployment

The app is ready to deploy on platforms like:
- Railway (free)
- Heroku
- PythonAnywhere
- Render

I've included `Procfile` and `railway.toml` for easy deployment.

## What I learned

Building this project helped me understand:
- Django framework basics
- API integration with requests library
- Frontend/backend communication
- Environment variables for security
- Responsive web design
- Error handling

## Future improvements

- Add weather alerts
- Save favorite locations
- Weather maps integration
- Historical weather data
- More detailed forecasts

## Issues?

If you run into any problems:
1. Make sure your API key is correct
2. Check internet connection
3. Verify all requirements are installed
4. Look at browser console for JavaScript errors

## License

Feel free to use this code for learning or your own projects!

