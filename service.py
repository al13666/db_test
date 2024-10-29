from flask import Flask
import psycopg2
from flask import request


app = Flask("TEST")


def get_db_connection():
    conn = psycopg2.connect(host='localhost', database = 'db', user = 'admin', password ='password1')
    return conn

@app.route('/find_user')
def find_user():
    conn = get_db_connection()
    cur = conn.cursor()

    name_user= request.args.get('name')
    request_to_db = "SELECT * FROM users WHERE name = '"+ name_user+ "';"

    cur.execute(request_to_db)
    users = cur.fetchall()
    cur.close()
    conn.close()
    res = ''
    for user in users:
        res += str(user) + '\n'
    return res



if __name__ == '__main__':
    app.run(debug=True)



