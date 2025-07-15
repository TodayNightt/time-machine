from config import API_KEY, ASSETS_DIR
from flask import Flask, request, send_from_directory


from common.api.time_machine import On_this_day
from common.dbs.history import exportJson, deleteHistory


app = Flask(__name__, static_folder="../frontend/dist", static_url_path="/")


@app.route('/on_this_day', methods=['POST'])
def on_this_day():
    day = request.json['day']

    month = request.json['month']
    year = int(request.json['year'])
    date = f'{month}/{day}'
    data = On_this_day(date, year)
    return data.returnJson()


@app.route('/db/get')
def dbs_show():
    return exportJson()


@app.route('/db/clear')
def dbs_clear():
    deleteHistory()
    return 'Done Clearing'


@app.route('/')
def serve_react():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == "__main__":
    if (API_KEY is None or ASSETS_DIR is None):
        print("API_KEY and ASSETS_DIR envs needed to be set")
        exit(1)

    app.run()
