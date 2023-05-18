from flask import Flask, jsonify
import requests

app = Flask(__name__)

API_KEY = 'c4153e8753bcd141ed7ad7856f7a185f'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({'error': 'Unable to get weather data'})

if __name__ == "__main__":
    app.run(debug=True)