from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')

        return '''<h1>The name is: {}</h1>
                  <h1>The age is: {}</h1>'''.format(name, age)

    return '''<form method="POST">
                  Name: <input type="text" name="name"><br>
                  Age: <input type="text" name="age"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

if __name__ == '__main__':
    app.run(debug=True)
