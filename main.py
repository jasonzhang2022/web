from flask import  render_template

def index(request):
    return render_template("input.html")


def calculate(request):
    num = int(request.form["num"])
    result = num*num
    return render_template("result.html", result=result)


