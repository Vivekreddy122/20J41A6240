import json
import requests

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/trains', methods=['GET'])
def get_trains():
  # Fetch train data from the database
  train_data = [
    {
      "t_Name": "Chennai Exp",
      "t_Number": "2344",
      "d_Time": "21:35",
      "a_Time": "23:55",
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
      "t_Name": "Hyd Exp",
      "t_Number": "2341",
      "d_Time": "23:55",
      "a_Time": "05:55",
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


  filtered_train_data = [train for train in train_data if train['d_Time'] > '21:55']
  filtered_train_data.sort(key=lambda train: (train['price'], train['seatAvailability']['sleeper'], -train['d_Time']))

  return json.dumps(filtered_train_data)

if __name__ == '__main__':
  app.run(debug=True)
