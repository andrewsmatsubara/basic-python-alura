import requests
import json
import os

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

if response.status_code == 200:
  data = response.json()
  restaurant_data = {}

  for item in data:
    restaurant_name = item['Company']

    if restaurant_name not in restaurant_data:
      restaurant_data[restaurant_name] = []

    restaurant_data[restaurant_name].append({
      "item": item['Item'],
      "price": item['price'],
      "description": item['description']
    })
else:
  print(response.status_code)

for restaurant_name, data in restaurant_data.items():
  filename = f'{restaurant_name}.json'
  with open(f'python_project/restaurants_json/{filename}', 'w') as restaurant_file:
    json.dump(data, restaurant_file, indent = 4)