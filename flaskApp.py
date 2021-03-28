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

# @app.route('/greenhouse', methods=['POST'])
# def greenhouse():
#     c = request.form.get('cols')
#     r = request.form.get('rows')
#     if (c.isnumeric() and r.isnumeric() and int(r) > 0 and int(c) > 0):
#         globalCols = int(c)
#         globalRows = int(r)
#         if globalCols > 10:
#             globalCols = 10
#             message = "Max cols is 10."
#         if globalRows > 1000:
#             globalRows = 1000
#             message = "Max rows is 1000."
#     else:
#         globalCols = 0
#         globalRows = 0
#     return render_template("index.html", cols=globalCols, rows=globalRows, message=globalMessage, seq=globalSeq)


@app.route('/generate', methods=['POST'])
def gen():
    globalSeq = []
    globalCols = int(request.form.get('cols', 0))
    globalRows = int(request.form.get('rows', 0))

    if (int(globalRows) > 0 and int(globalCols) > 0):
        if globalCols > 10:
            globalCols = 10
            message = "Max cols is 10."
        if globalRows > 1000:
            globalRows = 1000
            message = "Max rows is 1000."
        globalSeq = [["" for j in range(globalRows)] for i in range(globalCols)]

    print(request.form.get('matrix-indicator'))
    if request.form.get('matrix-indicator'):
        for x in range(globalCols):
            for y in range(globalRows):
                # print(request.form.get((str(x)+','+str(y)), ""))
                globalSeq[x][y] = request.form.get((str(x)+','+str(y)), "")
        # SEND OUTPUT HERE
    return render_template("index.html", cols=globalCols, rows=globalRows, message=globalMessage, seq=globalSeq)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html", cols=0, rows=0, message="", seq=[])


if __name__ == "__main__":
    app.run(debug=True)