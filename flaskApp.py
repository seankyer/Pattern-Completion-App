from flask import Flask, render_template, url_for, request, redirect, g

# mainfile = __import__("main.py")
# generate = mainfile.generate

def generate(seq, subsetRow, subsetCol, dir, n):
    return [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

app = Flask(__name__)

globalCols = 0
globalRows = 0
globalMessage = ""
globalSeq = []

@app.route('/greenhouse', methods=['POST'])
def greenhouse():
    c = request.form.get('cols')
    r = request.form.get('rows')
    if (c.isnumeric() and r.isnumeric() and int(r) > 0 and int(c) > 0):
        globalCols = int(c)
        globalRows = int(r)
        if globalCols > 10:
            globalCols = 10
            message = "Max cols is 10."
        if globalRows > 1000:
            globalRows = 1000
            message = "Max rows is 1000."
    else:
        globalCols = 0
        globalRows = 0
    return render_template("index.html", cols=globalCols, rows=globalRows, message=globalMessage, seq=globalSeq)


@app.route('/generate', methods=['POST'])
def gen():
    # print(dir(app.app_context()))
    # print(dict(g))
    # print(app.request))
    # seq = []
    cols = 1; rows = 1 # How to get these numbers from the HTML?
    for x in range(globalCols):
        for y in range(globalRows):
            print("what")
    # if valid_input():
        # print("what")
        # determine_direction() ???
        # out = generate(request.form['seq'],request.form['rows'], request.form['cols'], 'u', 0)
    return render_template("index.html", cols=globalCols, rows=globalRows, message=globalMessage, seq=globalSeq)


@app.route('/')
def index():
    return render_template("index.html", cols=globalCols, rows=globalRows, message=globalMessage, seq=globalSeq)


if __name__ == "__main__":
    app.run(debug=True)


def valid_input(seq, rows, cols):
    return True


# seann wyd
# @app.route('/success/<name>')
# def success(name):
#     return 'welcome %s' % name

# @app.route('/test', methods=['GET', 'POST'])
# def test_button():
#     if request.method == 'POST':
#         user = request.form['name']
#         return redirect(url_for('success', name=user))
