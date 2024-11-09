from flask import Blueprint, request, Response, Flask
import psycopg2
import json
from psycopg2.extras import DictCursor
from database import get_db_connection, load_sql_query
import os
from flask import jsonify
import functools



bp = Blueprint('relation', __name__, url_prefix='/relation')


@bp.route('/', methods=['GET', 'POST', 'DELETE'], strict_slashes = False)
def relation():
    if request.method == 'POST':
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=DictCursor)

        if request.is_json:
            data = request.get_json()
            name_user = data.get('name')
            name_achievement = data.get('name_achievement')

        
        request_to_db = load_sql_query("user_id_by_name.sql")
        cur.execute(request_to_db, (name_user,))
        user_result = cur.fetchone()  
        if user_result:
            user_id = user_result['id']
        else:
            return 'User not found', 404

        request_to_db = load_sql_query("acievement_id_by_name.sql")
        cur.execute(request_to_db, (name_achievement,))
        achievement_result = cur.fetchone()  
        if achievement_result:
            achievement_id = achievement_result['id']
        else:
            return 'Achievement not found', 404

        
        request_to_db = load_sql_query("insert_relation.sql")
        cur.execute(request_to_db, (user_id, achievement_id))
        conn.commit()

        cur.close()
        conn.close()

        res = f'Achievement "{name_achievement}" given to user "{name_user}"'
        return res