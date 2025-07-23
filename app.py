cd ~/Desktop/EagleNet003 && \
cat > dashboard/app.py <<'EOF'
import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)

# SQLite Database Configuration
DATABASE = 'eaglenet.db'

def get_db():
    """Create and return a SQLite database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Enable dictionary-style access
    return conn

def init_db():
    """Initialize database tables"""
    with get_db() as conn:
        conn.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        conn.commit()

# Initialize database on startup
init_db()

@app.route('/')
def home():
    """Example endpoint that returns data"""
    try:
        with get_db() as conn:
            items = conn.execute('SELECT * FROM items LIMIT 10').fetchall()
        return jsonify([dict(item) for item in items])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
EOF