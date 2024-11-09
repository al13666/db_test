from flask import Flask, Response
import psycopg2
from flask import request
import os
from flask import jsonify
import json
from psycopg2.extras import DictCursor
from routes import achievements, user, relation, show_user_achievements,statistic, hello


app = Flask("TEST")




app.register_blueprint(hello.bp)
app.register_blueprint(achievements.bp)
app.register_blueprint(user.bp)
app.register_blueprint(relation.bp)
app.register_blueprint(show_user_achievements.bp)
app.register_blueprint(statistic.bp)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)



