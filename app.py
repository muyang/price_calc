from model import InputForm
from flask import Flask, render_template, request
from compute import *

from werkzeug import secure_filename

eu2us = 1.15
us2rmb = 6.5
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	form = InputForm(request.form)
	if request.method == 'POST' and form.validate():
		CBM=getCBM(form.l.data, form.w.data, form.h.data)
		price1 = getPrePrice(form.PLZ.data, CBM, form.Weight.data)
		price2 = getPostPrice(form.Province.data, form.City.data, CBM, form.Weight.data)		
		#result = compute(form.A.data, form.b.data,form.w.data, form.T.data)
		
		FOG = CBM * 120
		ISPS = 2.5
		Un_loading = 31.5* form.Weight.data / 1000
		CFS = 12 * CBM
		Anti_Terror = 3
		#Pickup = 200 * eu2us
		Custom_clearance = 300.0 / us2rmb
		price3=price1 * eu2us + price2 / 6.5 + (FOG +ISPS + Un_loading + CFS + Anti_Terror + Custom_clearance)

	else:
		price1 = None
		price2 = None
		price3 = None
		#result = None
	
	return render_template('view_plain.html', form=form, price1=price1, price2=price2, price3=price3)
	#return render_template('view_plain.html', form=form, result=result, price=price)

'''
@app.route('/upload')
def upload_file():
	return render_template('upload.html')
'''

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
	form = InputForm(request.form)
	if request.method == 'POST' and form.validate():
		result = compute(form.A.data, form.b.data,
							form.w.data, form.T.data)
	else:
		result = None
	return render_template('view_plain.html', form=form, result=result)

if __name__ == '__main__':
	app.run(debug=True)
