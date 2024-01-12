from __init__ import app
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
import mysql.connector
from models.database import connection, cursor
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        email = request.form['email']
        senha = request.form['senha']
        cursor.execute(f"SELECT * FROM users WHERE email = '{email}' and senha = '{senha}'")
        rows = cursor.rowcount
        if rows < 1:
            alertMsg = "Email ou senha invalidos."
            alertClass = "alert alert-danger"
        return render_template('login.html')
    return render_template('login.html')