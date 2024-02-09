import requests

api_key = 'dd99368831271f12aaabbb82f461e225'

user_input = input('Enter a city: ')

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&appid={api_key}")

if weather_data.json()['cod'] == '404':
    print("This city doesn't exist!")
    exit()

weather = weather_data.json()['weather'][0]['main']
main_temp = weather_data.json()['main']['temp']
feels_like_temp = weather_data.json()['main']['feels_like']
country = weather_data.json()['sys']['country']


print(f'The weather in {user_input}, {country} is: {weather}.')
print(f'The temperature is {main_temp}°C, feels like {feels_like_temp}°C.')