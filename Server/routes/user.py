from flask import Blueprint, request, Response, Flask
import psycopg2
import json
from psycopg2.extras import DictCursor
from database import get_db_connection, load_sql_query
import os
from flask import jsonify
import functools



bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/', methods = ['GET', 'POST', 'DELETE'])
def find_user():
    if request.method=='GET':
        
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=DictCursor)
        name_user= request.args.get('name')
        
        request_to_db = load_sql_query("users_by_name.sql")

        cur.execute(request_to_db, (name_user,))
        user = cur.fetchall()
        cur.close()
        conn.close()
        res = [
            {"id": us["id"], "name": us["name"], "language": us["language"]}
            for us in user
        ]
        return Response(json.dumps(res, ensure_ascii=False, indent=4), content_type="application/json")