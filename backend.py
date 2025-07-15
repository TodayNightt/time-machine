from config import API_KEY
from flask import Flask, request


from api.time_machine import On_this_day
from dbs.history import exportJson, deleteHistory


app = Flask(__name__)


@app.route('/on_this_day', methods=['POST'])
def on_this_day():
    day = request.json['day']

    month = request.json['month']
    year = int(request.json['year'])
    date = f'{month}/{day}'
    data = On_this_day(date, year)
    return data.returnJson()


@app.route('/dbs_show')
def dbs_show():
    return exportJson()


@app.route('/dbs_clear')
def dbs_clear():
    deleteHistory()
    return 'Done Clearing'


if __name__ == "__main__":
    if (API_KEY is None):
        print("API_KEY is required")
        exit(1)

    app.run(port=5000, host='127.0.0.1')
