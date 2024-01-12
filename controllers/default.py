from __init__ import app
from flask import render_template
from flask import redirect
from flask import url_for
import mysql.connector
from models.database import connection, cursor
@app.route('/')
def index():
    return render_template('index.html')