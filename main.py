from flask import Flask, request, render_template_string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']

        if not name or not age.isdigit():
            return "Invalid input.", 400

        new_entry = Entry(name=name, age=int(age))
        db.session.add(new_entry)
        db.session.commit()

        return 'Entry added: Name: {}, Age: {}'.format(name, age)

    return '''<form method="POST">
                  Name: <input type="text" name="name"><br>
                  Age: <input type="text" name="age"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

if __name__ == '__main__':
    app.run(debug=True)
