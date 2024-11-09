from flask import Blueprint, request, Response, Flask
import psycopg2
import json
from psycopg2.extras import DictCursor
from database import get_db_connection, load_sql_query
import os
from flask import jsonify
import functools



bp = Blueprint('show_user_achievements', __name__, url_prefix='/show_user_achievements')



@bp.route('/<string:name_user>')
def show_user_achievements(name_user):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=DictCursor)

    request_to_db = load_sql_query("show_user_achievements.sql")
    
    cur.execute(request_to_db, (name_user,))
    user_achievements = cur.fetchall()

    cur.close()
    conn.close()
    res = ''
    res = [
        {"name": achiev["user_full_name"], "time": achiev["achievement_time"], "achievement": achiev["achievement_name"]}
        for achiev in user_achievements
    ]
    return Response(json.dumps(res, ensure_ascii=False, indent=4), content_type="application/json")