cat > dashboard/app.py <<'EOF'
import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)
DATABASE = 'eaglenet.db'

@app.route('/')
def home():
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        conn.close()
        return jsonify({"status": "success", "tables": tables})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run()
EOF