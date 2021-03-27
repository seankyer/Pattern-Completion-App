from flask import Flask, render_template, url_for, request, redirect, session

# mainfile = __import__("main.py")
# generate = mainfile.generate



def generate(seq, subsetRow, subsetCol, dir, n):
    return [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    print("hi")


app = Flask(__name__)


# @app.route('/generate', methods=['POST'])
# def gen():
#     if valid_input(request.form['rows'], request.form['cols'], request.form['seq']):
#         session['row'] = 5
#         # determine_direction() ???
#         out = generate(request.form['seq'],request.form['rows'], request.form['cols'], 'u', 0)
#         return render_template("index.html", output=out)


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/test', methods=['GET', 'POST'])
def test_button():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('success', name=user))


@app.route('/')
def index():
    return render_template("index.html", generateFn=generate)


if __name__ == "__main__":
    app.run(debug=True)
