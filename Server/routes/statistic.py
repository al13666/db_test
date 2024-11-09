from flask import Blueprint, request, Response, Flask
import psycopg2
import json
from psycopg2.extras import DictCursor
from database import get_db_connection, load_sql_query
import os
from flask import jsonify
import functools



bp = Blueprint('statistic', __name__, url_prefix='/statistic')

@bp.route('/<string:function>')
def statistic(function):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=DictCursor)

    if function == "max_count_achievements":
    
        request_to_db = load_sql_query("statistic_max_count_achievements.sql")
        
        cur.execute(request_to_db)
        user_achievements_count = cur.fetchall()

        cur.close()
        conn.close()
        res = [
            {"name": uac["user_full_name"], "count_achievements": uac["achievement_count"]}
            for uac in user_achievements_count
        ]
        return Response(json.dumps(res, ensure_ascii=False, indent=4), content_type="application/json")

    elif function=="max_points_achievements":
        request_to_db = load_sql_query("statistic_max_points_achievements.sql")

        cur.execute(request_to_db)
        user_achievements_points = cur.fetchall()

        cur.close()
        conn.close()
        res = ''
        res = [
            {"name": uap["user_full_name"], "points_achievements": uap["total_points"]}
            for uap in user_achievements_points
        ]
        return Response(json.dumps(res, ensure_ascii=False, indent=4), content_type="application/json")

    elif function=="max_points_difference":
        request_to_db = load_sql_query("statistic_max_points_difference.sql")
        
        cur.execute(request_to_db)
        users_max_points_diff = cur.fetchall()

        cur.close()
        conn.close()
        res = [
            {"user1": umpd["user1_name"], "points_user1": umpd["user1_points"], 
            "user2": umpd["user2_name"], "points_user2": umpd["user2_points"],
            "difference_points" : umpd["point_difference"]}
            for umpd in users_max_points_diff
        ]
        return Response(json.dumps(res, ensure_ascii=False, indent=4), content_type="application/json")

    elif function=="min_points_difference":
        request_to_db = load_sql_query("statistic_min_points_difference.sql")

        cur.execute(request_to_db)
        users_min_points_diff = cur.fetchall()

        cur.close()
        conn.close()
        res = [
            {"user1": umpd["user1_name"], "points_user1": umpd["user1_points"],
            "user2": umpd["user2_name"], "points_user2": umpd["user2_points"],
            "difference_points" : umpd["point_difference"]}
            for umpd in users_min_points_diff
        ]
        return Response(json.dumps(res, ensure_ascii=False, indent=4), content_type="application/json")

    elif function=="got_achievements_7_days_in_row":
        request_to_db = load_sql_query("statistic_got_achievements_7_days_in_row.sql")
        
        cur.execute(request_to_db)
        users = cur.fetchall()

        cur.close()
        conn.close()
        res = [
            {"name": u["user_name"]}
            for u in users
        ]
        return Response(json.dumps(res, ensure_ascii=False, indent=4), content_type="application/json")

    else:
        return "There are no such statistics yet"