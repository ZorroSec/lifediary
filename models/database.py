import mysql.connector

connection = mysql.connector.connect(
    host='monorail.proxy.rlwy.net',
    port=50276,
    user='railway',
    password='-AAlCJXn8k-pYilmi-wPzAbCpDbSq_lG',
    database='railway'
)

cursor = connection.cursor()