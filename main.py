# app.py
from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect(':memory:') 
    conn.execute('CREATE TABLE IF NOT EXISTS entries (name TEXT, age INTEGER)')
    return conn

@app.route('/', methods=['GET', 'POST'])
def form_example():
    conn = get_db_connection()
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']

        conn.execute('INSERT INTO entries (name, age) VALUES (?, ?)', (name, age))
        conn.commit()

        return '''<h1>Entry added:</h1>
                  <h2>Name: {}</h2>
                  <h2>Age: {}</h2>'''.format(name, age)
    conn.close()
    return '''<form method="POST">
                  Name: <input type="text" name="name"><br>
                  Age: <input type="text" name="age"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

if __name__ == '__main__':
    app.run(debug=True)
