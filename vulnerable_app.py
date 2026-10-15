from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

@app.route('/user')
def user():
    username = request.args.get('username', '')
    # FIXED: SQL Injection - parameterized query
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    result = cursor.fetchall()
    return str(result)

@app.route('/greet')
def greet():
    name = request.args.get('name', '')
    # FIXED: XSS - template auto-escaping
    return render_template_string("<h1>Hello {{ name }}</h1>", name=name)

if __name__ == '__main__':
    app.run(debug=False)  # FIXED: debug disabled
