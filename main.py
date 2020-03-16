from flask import  render_template

def index(request):
    return render_template("input.html")



def addnumber(num):
    sum = 0
    for x in range(1, num + 1):
        sum = sum + x
    return sum

def calculate(request):
    num = 0
    result = 0
    if request.form and request.form["num"]:
        num = int(request.form["num"])
        result = addnumber(num)
    return render_template("result.html", result=result, num=num)
