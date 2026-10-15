The vulnerability in this code is in line 10-13(sql_injection).
The risk is very critical and need to be fixed immediately.
To fix this, I used parameterized queries.
Following is the before code that's vulnerable to sql_injection:

from flask import Flask, request, render_template_string
import sqlite3
app = Flask(__name__)
@app.route('/user')
def user():
    username = request.args.get('username', '')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchall()
    return str(result)
@app.route('/greet')
def greet():
    name = request.args.get('name', '')
    return render_template_string(f"<h1>Hello {name}</h1>")
if __name__ == '__main__':
    app.run(debug=True)
    



The fixed and secure version of the above code is given below:

from flask import Flask, request, render_template_string
import sqlite3
app = Flask(__name__)
@app.route('/user')
def user():
    username = request.args.get('username', '')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    result = cursor.fetchall()
    return str(result)
@app.route('/greet')
def greet():
    name = request.args.get('name', '')
    return render_template_string("<h1>Hello {{ name }}</h1>", name=name)
if __name__ == '__main__':
    app.run(debug=False)  # FIXED: debug disabled
