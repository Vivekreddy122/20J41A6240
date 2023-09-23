import json
import requests

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/trains', methods=['GET'])
def get_trains():
  # Fetch train data from the database
  train_data = [
    {
      "trainName": "Chennai Exp",
      "trainNumber": "2344",
      "departureTime": "21:35",
      "arrivalTime": "23:55",
      "seatAvailability": {
        "sleeper": 3,
        "AC": 1
      },
      "price": {
        "sleeper": 554,
        "AC": 1854
      },
      "delay": 15
    },
    {
      "trainName": "Hyderabad Exp",
      "trainNumber": "2341",
      "departureTime": "23:55",
      "arrivalTime": "05:55",
      "seatAvailability": {
        "sleeper": 6,
        "AC": 7
      },
      "price": {
        "sleeper": 666,
        "AC": 1966
      },
      "delay": 5
    }
  ]


  filtered_train_data = [train for train in train_data if train['departureTime'] > '21:55']

  # Order train data in ascending order of price, descending order of tickets, and descending order of departure time (after considering delays in minutes)
  filtered_train_data.sort(key=lambda train: (train['price'], train['seatAvailability']['sleeper'], -train['departureTime']))

  return json.dumps(filtered_train_data)

if __name__ == '__main__':
  app.run(debug=True)
