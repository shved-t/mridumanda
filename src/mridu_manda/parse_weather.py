from datetime import datetime



def weather_access(weather):
    
    city_weather = weather['name']
    country = weather['sys']['country']
    weather_id = weather['weather'][0]['id']
    condition = weather['weather'][0]['description'].title()
    temperature = weather['main']['temp']
    feels_like = weather['main']['feels_like']
    humidity = weather['main']['humidity']
    pressure = weather['main']['pressure']
    temperature_max = weather['main']['temp_max']
    temperature_min = weather['main']['temp_min']
    sunrise_time = datetime.fromtimestamp(weather['sys']['sunrise']).strftime('%H:%M:%S')
    sunset_time = datetime.fromtimestamp(weather['sys']['sunset']).strftime('%H:%M:%S')

    return [city_weather, country, weather_id, condition, temperature, feels_like, humidity, pressure, temperature_max, temperature_min, sunrise_time, sunset_time]


'''
    0  -> city
    1  -> country
    2  -> id
    3  -> condition
    4  -> temperature
    5  -> feels like
    6  -> humidity
    7  -> pressure
    8  -> temperature max
    9  -> temperature min
    10 -> sunrise time
    11 -> sunset time
'''