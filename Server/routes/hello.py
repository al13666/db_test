from flask import Blueprint, request, Response, Flask
import psycopg2
import json
from psycopg2.extras import DictCursor
from database import get_db_connection
import os
from flask import jsonify
import functools



bp = Blueprint('api', __name__, url_prefix='/')

@bp.route('/')
def hello():

    return "hello from db_test"