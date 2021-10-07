# !/usr/bin/env python3

import requests
import os
import math
import datetime
from pprint import pprint
# data = requests.get('https://catfact.ninja/fact').json()
# fact = data['fact']
# print(f'A random cat fact is: {fact}')


# bit_data = requests.get(
#     'https://api.coindesk.com/v1/bpi/currentprice.json').json()

# rate = bit_data['bpi']['USD']['rate_float']
# # print(rate)
# # print(bit_data)
# user = float(input('Enter a number of Bitcoin: '))
# total = rate * user
# print(f'The current Bitcoin price in USD is {total}')

key = os.environ.get('WEATHER_KEY')  # map of all env in os
weather_url = 'https://api.openweathermap.org/data/2.5/weather'
# Weather


def main():
    location = get_location()
    weather_data, error = get_current_weather(location, key)
    if error:
        print('Sorry, could not get weather')
    else:
        current_temp = get_temp(weather_data)
        print(f'The current temperature is {current_temp}C')


def get_location():
    city, country = '', ''
    while len(city) == 0:
        city = input('Enter the name of the city: ').strip()

    while len(country) != 2 or not country.isalpha():
        country = input('Enter the 2-letter country name: ').strip()

    location = f'{city}, {country}'
    return location


def get_current_weather(location, key):
    try:
        query = {'q': location, 'units': 'metric', 'appid': key}
        response = requests.get(weather_url, params=query)
        response.raise_for_status()  # raises 400 or 500 status code
        data = response.json()
        return data, None
    except Exception as err:
        print(err)
        print(response.txt)
        return None, err


def get_temp(weather_data):
    try:
        data_temp = weather_data['main']['temp']
        # data = weather_data['weather'][0]['description']
        # temp = math.floor(data_temp - 273.15)  # kelvin to fahrenheit
        # return (
        #     f'The weather today in {city} is {data}, the temperature is {1.8 * temp + 32:.0f}F.')
        return data_temp

    except KeyError as err:
        print('This data is not in the format expected')
        return 'Unkown'


if __name__ == '__main__':
    main()
