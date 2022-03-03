from flask import Flask, request, jsonify
from flask_cors import CORS
import neural_network
import datetime as dt

application = app = Flask(__name__)
CORS(app)

disponible_coins = ['BTC', 'ETH', 'SOL', 'ADA', 'XRP']
coins_data = {}
coins_predictions = {}
BTC_data = []
ETH_data = []
SOL_data = []
BTC_prediction = 0
SOL_prediction = 0
ETH_prediction = 0

@app.route('/get_data', methods=['GET'])
def get_data():
    formatted_data = {}
    predictions = {}

    for coin in disponible_coins:
        formatted_data[coin] = []
        predictions[coin] = float(coins_predictions[coin])

    for coin in disponible_coins:
        date = dt.datetime(2020, 1, 1)
        for item in coins_data[coin]:
            formatted_data[coin].append({
                'date': date,
                'price': item
            })
            date += dt.timedelta(days=1)

    return jsonify({'old_data': formatted_data, 'predictions': predictions})


@app.route('/')
def index():
    return 'ola'

@app.route('/train')
def train_data():
    print('la app entra y empieza')
    for coin in disponible_coins:
        coins_data[coin], coins_predictions[coin] = neural_network.train_data(coin)

    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    

    # BTC_data, BTC_prediction = neural_network.train_data('BTC')
    # ETH_data, ETH_prediction = neural_network.train_data('ETH')
    # SOL_data, SOL_prediction = neural_network.train_data('SOL')
    app.run(port=5000)

    