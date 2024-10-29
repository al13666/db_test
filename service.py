from flask import Flask
import psycopg2
from flask import request


app = Flask("TEST")


def get_db_connection():
    conn = psycopg2.connect(host='localhost', database = 'db', user = 'admin', password ='password1')
    return conn



@app.route('/show_achievements')
def show_achievements():
    conn = get_db_connection()
    cur = conn.cursor()

    
    request_to_db = "SELECT * FROM achievements;"
    cur.execute(request_to_db)
    achievements = cur.fetchall()
    cur.close()
    conn.close()
    res = ''
    for achievement in achievements:
        res += str(achievement) + '\n'
    return res

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

@app.route('/add_achievement')
def add_achievement():
    conn = get_db_connection()
    cur = conn.cursor()

    name_achievement= request.args.get('name')
    points_achievement= request.args.get('points')
    description_achievement= request.args.get('description')

    request_to_db = "INSERT INTO achievements (name, points, description) VALUES('" + name_achievement +"', "+points_achievement+",' "+description_achievement+"');"
    cur.execute(request_to_db)
    conn.commit()
    cur.execute('SELECT * FROM achievements;')
    achievements = cur.fetchall()
    cur.close()
    conn.close()
    res = 'hello'
    for achievement in achievements:
        res += str(achievement) + '\n'
    return res

if __name__ == '__main__':
    app.run(debug=True)



