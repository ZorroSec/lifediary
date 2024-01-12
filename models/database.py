import mysql.connector

connection = mysql.connector.connect(
    host='monorail.proxy.rlwy.net',
    port=49388,
    user='railway',
    pasword='lifediary',
    database='lifediary'
)

cursro = connection.cursor()