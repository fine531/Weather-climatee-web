# Climatee Weather App 🌤️

A simple weather web application built with Django that shows current weather and forecasts for any city. I created this project to learn Django and API integration.

## What it does

- Shows current weather (temperature, humidity, wind speed)
- Gets your location automatically or search any city
- Displays 24-hour forecast 
- Works on mobile and desktop

## Screenshots

The app has a clean interface with location detection and city search functionality. The weather data is displayed in an easy-to-read format with icons and detailed information.

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
