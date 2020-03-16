from flask import  render_template
from markupsafe import escape

app = flask.Flask(__name__)


def index(request):
    return render_template("input.html")


@app.route('/calculate', methods=['POST'])
def calculate(request):
    num = int(request.form["num"])
    result = num*num
    return render_template("result.html", result=result)


