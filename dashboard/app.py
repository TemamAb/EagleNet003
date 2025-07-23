import os
import psycopg2
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port="5432"
        )
        conn.close()
        return "EagleNet Dashboard Online"
    except Exception as e:
        return f"Database connection failed: {e}"

@app.route("/ping")
def ping():
    return "pong"

handler = app
