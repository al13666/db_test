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
    name_rus_achievement= request.args.get('name_rus')
    points_achievement= request.args.get('points')
    description_achievement= request.args.get('description')
    description_rus_achievement= request.args.get('description_rus')


    request_to_db = "INSERT INTO achievements (name, points, description, description_rus, name_rus) VALUES('" + name_achievement +"', "+points_achievement+",' "+description_achievement+",' "+description_rus_achievement+",' "+name_rus_achievement+"');"
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


@app.route('/add_relation')
def add_relation():
    conn = get_db_connection()
    cur = conn.cursor()

    name_user= request.args.get('user')
    request_to_db = "SELECT id FROM users WHERE name= '"+ name_user+ "';"
    cur.execute(request_to_db)
    user_id = cur.fetchall()

    name_achievement= request.args.get('achievement')
    request_to_db = "SELECT id FROM achievements WHERE name= '"+ name_achievement+ "';"
    cur.execute(request_to_db)
    achievement_id = cur.fetchall()


    request_to_db = "INSERT INTO user_achievement (time, user_id, achievement_id) VALUES(now(), "+str(user_id[0][0])+", "+str(achievement_id[0][0])+");"
    cur.execute(request_to_db)
    # ch = cur.fetchall()
    conn.commit()
    
    cur.close()
    conn.close()
    res = 'achievement '+ name_achievement+ ' given to user '+name_user
    # if(ch):
    #     for c in ch:
    #         res += str(c)

    return res


@app.route('/show_user_achievements')
def show_user_achievements():
    conn = get_db_connection()
    cur = conn.cursor()

    name_user= request.args.get('name')
    request_to_db = "SELECT u.name AS user_full_name, TO_CHAR(ua.time, 'YYYY-MM-DD HH24:MI:SS') AS achievement_time, CASE WHEN u.language = 'ru' THEN a.name_rus ELSE a.name END AS achievement_name FROM users u LEFT JOIN user_achievement ua ON ua.user_id = u.id LEFT JOIN achievements a ON a.id = ua.achievement_id WHERE u.name = '"+name_user+"';"
    cur.execute(request_to_db)
    user_achievements = cur.fetchall()

    cur.close()
    conn.close()
    res = ''
    for user_achievement in user_achievements:
        res += str(user_achievement) + '\n' 
    return res



@app.route('/show_user_max_count_achievements')
def show_user_max_count_achievements():
    conn = get_db_connection()
    cur = conn.cursor()
 
    request_to_db = "WITH user_achievement_count AS (SELECT u.id, u.name AS user_full_name, COUNT(ua.achievement_id) AS achievement_count FROM users u LEFT JOIN user_achievement ua ON ua.user_id = u.id GROUP BY u.id, u.name) SELECT user_full_name, achievement_count FROM user_achievement_count WHERE achievement_count = (SELECT MAX(achievement_count) FROM user_achievement_count);"
    cur.execute(request_to_db)
    user_achievements_count = cur.fetchall()

    cur.close()
    conn.close()
    res = ''
    for user_achievement in user_achievements_count:
        res += str(user_achievement) + '\n' 
    return res


@app.route('/show_user_max_points_achievements')
def show_user_max_points_achievements():
    conn = get_db_connection()
    cur = conn.cursor()
 
    request_to_db = "WITH user_achievement_max_points AS ( SELECT u.name AS user_full_name, SUM(a.points) AS total_points FROM users u LEFT JOIN user_achievement ua ON ua.user_id = u.id LEFT JOIN achievements a ON a.id = ua.achievement_id GROUP BY u.name) SELECT user_full_name, total_points FROM user_achievement_max_points WHERE total_points = (SELECT MAX(total_points) FROM user_achievement_max_points);"
    cur.execute(request_to_db)
    user_achievements_count = cur.fetchall()

    cur.close()
    conn.close()
    res = ''
    for user_achievement in user_achievements_count:
        res += str(user_achievement) + '\n' 
    return res


@app.route('/show_max_points_differences')
def show_max_points_differences():
    conn = get_db_connection()
    cur = conn.cursor()
 
    request_to_db = "WITH user_points AS (SELECT u.id AS user_id, u.name AS user_name, COALESCE(SUM(a.points),0) AS total_points FROM users u LEFT JOIN user_achievement ua ON ua.user_id = u.id LEFT JOIN achievements a ON a.id = ua.achievement_id GROUP BY u.id, u.name), points_differences AS( SELECT u1.user_name AS user1_name, u1.total_points AS user1_points, u2.user_name AS user2_name, u2.total_points AS user2_points, ABS (u1.total_points - u2.total_points) AS point_difference FROM user_points u1 JOIN user_points u2 ON u1.user_id <u2.user_id) SELECT user1_name, user1_points, user2_name, user2_points, point_difference FROM points_differences WHERE point_difference = (SELECT MAX(point_difference) FROM points_differences);"
    cur.execute(request_to_db)
    users_max_points_diff = cur.fetchall()

    cur.close()
    conn.close()
    res = ''
    for u in users_max_points_diff:
        res += str(u) + '\n' 
    return res

@app.route('/show_min_points_differences')
def show_min_points_differences():
    conn = get_db_connection()
    cur = conn.cursor()
 
    request_to_db = "WITH user_points AS (SELECT u.id AS user_id, u.name AS user_name, COALESCE(SUM(a.points),0) AS total_points FROM users u LEFT JOIN user_achievement ua ON ua.user_id = u.id LEFT JOIN achievements a ON a.id = ua.achievement_id GROUP BY u.id, u.name), points_differences AS( SELECT u1.user_name AS user1_name, u1.total_points AS user1_points, u2.user_name AS user2_name, u2.total_points AS user2_points, ABS (u1.total_points - u2.total_points) AS point_difference FROM user_points u1 JOIN user_points u2 ON u1.user_id <u2.user_id) SELECT user1_name, user1_points, user2_name, user2_points, point_difference FROM points_differences WHERE point_difference = (SELECT MIN(point_difference) FROM points_differences);"
    cur.execute(request_to_db)
    users_min_points_diff = cur.fetchall()

    cur.close()
    conn.close()
    res = ''
    for u in users_min_points_diff:
        res += str(u) + '\n' 
    return res


@app.route('/show_users_with_consecutive_achievements_7_days')
def show_users_with_consecutive_achievements_7_days():
    conn = get_db_connection()
    cur = conn.cursor()
 
    request_to_db = "WITH consecutive_achievements AS ( SELECT user_id, time::date AS achievement_date, ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY time::date) - EXTRACT(EPOCH FROM time::date) / (24 * 60 * 60) AS date_group FROM user_achievement GROUP BY user_id, time::date), streaks AS ( SELECT user_id, COUNT(*) AS days_in_a_row FROM consecutive_achievements GROUP BY user_id, date_group HAVING COUNT(*) >= 7) SELECT u.name AS user_name FROM users u JOIN streaks s ON u.id = s.user_id;"
    cur.execute(request_to_db)
    users_min_points_diff = cur.fetchall()

    cur.close()
    conn.close()
    res = ''
    for u in users_min_points_diff:
        res += str(u) + '\n' 
    return res

if __name__ == '__main__':
    app.run(debug=True)



