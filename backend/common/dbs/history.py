import sqlite3
import json
from pathlib import Path
import ast


dbs = 'db/search_history.sqlite3'

# Get search result and read it to the database


def writeHistory():

    datas = json.loads(Path('db/data.json').read_text())

    with sqlite3.connect(dbs) as conn:
        command = 'INSERT INTO search_history VALUES(?,?,?,?,?)'
        for data in datas:
            conn.execute(command, tuple(data.values()))
        conn.commit()


def deleteHistory():
    with sqlite3.connect(dbs) as conn:
        command = 'DELETE FROM search_history'
        conn.execute(command)


# Read from the database
def exportJson():
    item = []
    with sqlite3.connect(dbs) as conn:
        command = 'SELECT * FROM search_history'
        cursor = conn.execute(command)
        for rows in cursor:
            item.append([rows[0], ast.literal_eval(rows[1]),
                        ast.literal_eval(rows[2]), ast.literal_eval(rows[3]), ast.literal_eval(rows[4])])
    return item
