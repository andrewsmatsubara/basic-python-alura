from fastapi import FastAPI
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
  '''
  Endpoint to show a important message!
  '''
  return {'Hello': 'World'}

@app.get('/api/restaurants')
def get_restaurants(restaurant: str = None):
  '''
  Endpoint to show a list of restaurants data in case of lack of parameters.
  Shows a list of certain restaurant data if parameter is passed.
  '''
  url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
  response = requests.get(url)

  if response.status_code == 200:
    data = response.json()

    if restaurant is None:
      return {'Data': data}

    restaurant_data = []

    for item in data:
      if item['Company'] in restaurant:
        restaurant_data.append({
          "item": item['Item'],
          "price": item['price'],
          "description": item['description']
        })

    return {'Restaurant': restaurant, 'Menu': restaurant_data}
  else:
    return {'Error': f'{response.status_code} - {response.text}'}