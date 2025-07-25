"""Weather app views"""
import json
from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse
from .utils import fetch_weather, fetch_weather_by_coordinates


def weather_view(request):
    """Main view for weather app - handles both city search and location detection"""
    context = {
        'weather_data': None,
        'location_searched': None,
        'error': None
    }

    if request.method == 'POST':
        location = request.POST.get('location', '').strip()

        if not location:
            context['error'] = "Please enter a location."
            return render(request, 'weather/index.html', context)

        try:
            weather_data = fetch_weather(location)
            context['weather_data'] = weather_data
            context['location_searched'] = location

            messages.success(request,
                           f"Weather data for {weather_data['current']['location']} "
                           f"retrieved successfully!")

        except Exception as error:
            error_message = str(error)
            context['error'] = error_message
            context['location_searched'] = location
            messages.error(request, f"Error: {error_message}")

    return render(request, 'weather/index.html', context)


def refresh_weather(request):
    """AJAX endpoint for refreshing weather data without full page reload."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            location = data.get('location', '').strip()

            if not location:
                return JsonResponse({
                    'success': False,
                    'error': 'Please enter a location.'
                })

            weather_data = fetch_weather(location)

            return JsonResponse({
                'success': True,
                'data': weather_data,
                'location': location
            })

        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'error': 'Invalid request format.'
            })

        except Exception as error:
            return JsonResponse({
                'success': False,
                'error': str(error)
            })

    return JsonResponse({
        'success': False,
        'error': 'Method not allowed.'
    })


def weather_by_location(request):
    """AJAX endpoint for getting weather by coordinates (latitude/longitude)."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            latitude = data.get('latitude')
            longitude = data.get('longitude')

            if not latitude or not longitude:
                return JsonResponse({
                    'success': False,
                    'error': 'Invalid coordinates provided.'
                })

            weather_data = fetch_weather_by_coordinates(latitude, longitude)

            return JsonResponse({
                'success': True,
                'data': weather_data,
                'location_name': weather_data['current']['location']
            })

        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'error': 'Invalid request format.'
            })

        except Exception as error:
            return JsonResponse({
                'success': False,
                'error': str(error)
            })

    return JsonResponse({
        'success': False,
        'error': 'Method not allowed.'
    })
