from flask import Flask, render_template, request
#from compute import compute
from model import InputForm

app = Flask(__name__)

@app.route('/hw1', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        r = form.r.data
        s = compute(r)
        a = form.a.data
        b = form.b.data
        s_add = add(a,b)
		s =(s,s_add)
    else:
        s = None
    return render_template("view01.html", form=form, s=s)

#compute
import math
def compute(r):
    return math.sin(r)

def add(a,b):
    return a+b
	
if __name__ == '__main__':
    app.run(debug=True)
