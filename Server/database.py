import psycopg2
from psycopg2.extras import DictCursor
import os
from pathlib import Path


def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        database = os.getenv('POSTGRES_DB'),
        user = os.getenv("POSTGRES_USER"),
        password =os.getenv("POSTGRES_PASSWORD"))
    return conn



def load_sql_query(filename):
    
    base_dir = os.path.dirname(os.path.abspath(__file__))  
    file_path = os.path.join(base_dir, "queries", filename)
    with open(file_path, "r") as file:
        sql_query = file.read()
    return sql_query
