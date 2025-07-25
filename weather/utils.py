"""Weather API utilities"""
import os
from datetime import datetime
import requests


def fetch_weather(location):
    """Fetch weather data for a city - returns current weather and forecast"""
    api_key = os.getenv('OPENWEATHER_API_KEY', 'fb3e82b296f55d0382210c216d8149bf')

    forecast_url = "https://api.openweathermap.org/data/2.5/forecast"
    current_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        current_response = requests.get(current_url, params=params, timeout=10)
        current_response.raise_for_status()
        current_data = current_response.json()

        forecast_response = requests.get(forecast_url, params=params, timeout=10)
        forecast_response.raise_for_status()
        forecast_data = forecast_response.json()

        current_weather = {
            'location': current_data['name'],
            'country': current_data['sys']['country'],
            'temperature': round(current_data['main']['temp']),
            'description': current_data['weather'][0]['description'].title(),
            'wind_speed': current_data['wind']['speed'],
            'humidity': current_data['main']['humidity'],
            'icon': current_data['weather'][0]['icon']
        }

        if 'rain' in current_data:
            current_weather['rain_probability'] = current_data['rain'].get('1h', 0)
        else:
            current_weather['rain_probability'] = 0

        forecast_list = []
        for forecast_item in forecast_data['list'][:8]:
            forecast_time = datetime.fromtimestamp(forecast_item['dt'])
            forecast_entry = {
                'time': forecast_time.strftime('%H:%M'),
                'date': forecast_time.strftime('%m/%d'),
                'temperature': round(forecast_item['main']['temp']),
                'description': forecast_item['weather'][0]['description'].title(),
                'wind_speed': forecast_item['wind']['speed'],
                'icon': forecast_item['weather'][0]['icon']
            }

            if 'rain' in forecast_item:
                forecast_entry['rain_probability'] = forecast_item['rain'].get('3h', 0)
            else:
                forecast_entry['rain_probability'] = 0

            forecast_list.append(forecast_entry)

        return {
            'current': current_weather,
            'forecast': forecast_list,
            'success': True
        }

    except requests.exceptions.HTTPError as http_error:
        if http_error.response.status_code == 404:
            raise Exception(f"Location '{location}' not found. Please check the spelling and try again.")
        elif http_error.response.status_code == 401:
            raise Exception("Invalid API key. Please check your OpenWeather API key in the .env file. Get a free key at https://openweathermap.org/api")
        else:
            raise Exception(f"API Error: {http_error.response.status_code}")

    except requests.exceptions.ConnectionError:
        raise Exception("Connection error. Please check your internet connection.")

    except requests.exceptions.Timeout:
        raise Exception("Request timeout. Please try again.")

    except requests.exceptions.RequestException as req_error:
        raise Exception(f"Request failed: {str(req_error)}")

    except KeyError as key_error:
        raise Exception(f"Unexpected API response format: {str(key_error)}")

    except Exception as error:
        if "401" in str(error):
            raise Exception("Invalid API key. Please get a free API key from https://openweathermap.org/api and update your .env file")
        raise Exception(f"An error occurred: {str(error)}")


def fetch_weather_by_coordinates(latitude, longitude):
    """Fetch weather data using GPS coordinates"""
    api_key = os.getenv('OPENWEATHER_API_KEY', 'fb3e82b296f55d0382210c216d8149bf')

    forecast_url = "https://api.openweathermap.org/data/2.5/forecast"
    current_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        'lat': latitude,
        'lon': longitude,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        current_response = requests.get(current_url, params=params, timeout=10)
        current_response.raise_for_status()
        current_data = current_response.json()

        forecast_response = requests.get(forecast_url, params=params, timeout=10)
        forecast_response.raise_for_status()
        forecast_data = forecast_response.json()

        current_weather = {
            'location': current_data['name'],
            'country': current_data['sys']['country'],
            'temperature': round(current_data['main']['temp']),
            'description': current_data['weather'][0]['description'].title(),
            'wind_speed': current_data['wind']['speed'],
            'humidity': current_data['main']['humidity'],
            'icon': current_data['weather'][0]['icon']
        }

        if 'rain' in current_data:
            current_weather['rain_probability'] = current_data['rain'].get('1h', 0)
        else:
            current_weather['rain_probability'] = 0

        forecast_list = []
        for forecast_item in forecast_data['list'][:8]:
            forecast_time = datetime.fromtimestamp(forecast_item['dt'])

            forecast_entry = {
                'time': forecast_time.strftime('%H:%M'),
                'date': forecast_time.strftime('%m/%d'),
                'temperature': round(forecast_item['main']['temp']),
                'description': forecast_item['weather'][0]['description'].title(),
                'wind_speed': forecast_item['wind']['speed'],
                'icon': forecast_item['weather'][0]['icon']
            }

            if 'rain' in forecast_item:
                forecast_entry['rain_probability'] = forecast_item['rain'].get('3h', 0)
            else:
                forecast_entry['rain_probability'] = 0

            forecast_list.append(forecast_entry)

        return {
            'current': current_weather,
            'forecast': forecast_list,
            'success': True
        }

    except requests.exceptions.HTTPError as http_error:
        if http_error.response.status_code == 404:
            raise Exception("Location not found for the provided coordinates.")
        elif http_error.response.status_code == 401:
            raise Exception("Invalid API key. Please check your OpenWeather API key in the .env file. Get a free key at https://openweathermap.org/api")
        else:
            raise Exception(f"API Error: {http_error.response.status_code}")

    except requests.exceptions.ConnectionError:
        raise Exception("Connection error. Please check your internet connection.")

    except requests.exceptions.Timeout:
        raise Exception("Request timeout. Please try again.")

    except requests.exceptions.RequestException as req_error:
        raise Exception(f"Request failed: {str(req_error)}")

    except KeyError as key_error:
        raise Exception(f"Unexpected API response format: {str(key_error)}")

    except Exception as error:
        if "401" in str(error):
            raise Exception("Invalid API key. Please get a free API key from https://openweathermap.org/api and update your .env file")
        raise Exception(f"An error occurred: {str(error)}")
