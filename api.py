from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database setup
def setup_db():
    with sqlite3.connect('users.db') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )''')
        conn.commit()

setup_db()

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    password = data['password']

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    with sqlite3.connect('users.db') as conn:
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    with sqlite3.connect('users.db') as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        
    if user:
        return jsonify({'message': 'Login successful', 'user_id': user[0]})
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/get_user_id', methods=['GET'])
def get_user_id():
    username = request.args.get('username')

    with sqlite3.connect('users.db') as conn:
        c = conn.cursor()
        c.execute("SELECT id FROM users WHERE username=?", (username,))
        user_id = c.fetchone()

    if user_id:
        return jsonify({'user_id': user_id[0]})
    else:
        return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
