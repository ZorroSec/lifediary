from app import app
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
        results = cursor.fetchall()
        print(rows)
        print(results)
        if rows > -1:
            alertMsg = "Email ou senha invalidos."
            alertClass = "alert alert-danger"
            return render_template('login.html', alertMsg=alertMsg, alertClass=alertClass)
        else:
            print(results)
            return redirect(f'/{results[0][1]}')
    return render_template('login.html')

@app.route('/<nome>', methods=['GET', 'POST'])
def console(nome):
    cursor.execute('SELECT * FROM posts ORDER BY likes DESC')
    res = cursor.fetchall()
    return render_template("index.html", nome=nome, results=res)
    # return "Success"