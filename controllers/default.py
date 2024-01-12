from __init__ import app
from flask import render_template
from flask import redirect
from flask import url_for
import mysql.connector
from models.database import connection, cursor
@app.route('/')
def index():
    cursor.execute('select * from users')
    results = cursor.fetchall()
    print(results)
    return 'Hello friend'