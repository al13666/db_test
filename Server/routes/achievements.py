from flask import Blueprint, request, Response, Flask
import psycopg2
import json
from psycopg2.extras import DictCursor
from database import get_db_connection, load_sql_query
import os
from flask import jsonify
import functools



bp = Blueprint('achievements', __name__, url_prefix='/achievements')

@bp.route('/', methods = ['GET', 'POST', 'DELETE'], strict_slashes = False)
def achievements():
    if request.method=='GET':
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=DictCursor)

        
        request_to_db = load_sql_query("achievements_get.sql")
        cur.execute(request_to_db)
        achievements = cur.fetchall()
        res = [
            {"id": achiev["id"], "name": achiev["name"], "points": achiev["points"], "description": achiev["description"], "description_rus": achiev["description_rus"], "name_rus": achiev["name_rus"]}
            for achiev in achievements
        ]
        cur.close()
        conn.close()

        return Response(json.dumps(res, ensure_ascii=False, indent=4), content_type="application/json")
    

    elif request.method == 'POST':
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=DictCursor)

        if request.is_json:
            data = request.get_json()
            name_achievement= data.get('name')
            name_rus_achievement= data.get('name_rus')
            points_achievement= data.get('points')
            description_achievement= data.get('description')
            description_rus_achievement= data.get('description_rus')


        request_to_db = load_sql_query("achievements_post.sql")
        cur.execute(request_to_db, (name_achievement, points_achievement, description_achievement, description_rus_achievement, name_rus_achievement))
        conn.commit()

        cur.execute('SELECT * FROM achievements;')
        achievements = cur.fetchall()
        cur.close()
        conn.close()
        res = [
            {"id": achiev["id"], "name": achiev["name"], "points": achiev["points"], "description": achiev["description"], "description_rus": achiev["description_rus"], "name_rus": achiev["name_rus"]}
            for achiev in achievements
        ]
        return Response(json.dumps(res, ensure_ascii=False, indent=4), content_type="application/json")