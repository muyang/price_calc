from model import InputForm
from flask import Flask, render_template, request
from compute import *

from werkzeug import secure_filename

# eu2us = 1.15
# us2rmb = 6.5
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	form = InputForm(request.form)
	if request.method == 'POST' and form.validate():
		CBM=getCBM(form.l.data, form.w.data, form.h.data)
		price1 = getPrePrice(form.PLZ.data, CBM, form.Weight.data)
		price2 = getPostPrice(form.Province.data, form.City.data, CBM, form.Weight.data)		
		#result = compute(form.A.data, form.b.data,form.w.data, form.T.data)
		eu2us = form.eu2us.data
		us2rmb = form.us2rmb.data
		
		FOG = CBM * form.FOG.data
		ISPS = form.ISPS.data
		Un_loading = form.Weight.data * form.Un_loading.data
		CFS = CBM * form.CFS.data
		Anti_Terror = form.Terror.data
		Cargo_Service = form.Cargo.data
		#Pickup = 200 * eu2us
		Custom_clearance = form.Custom.data / us2rmb

		price3=price1 * eu2us + price2 / us2rmb + (FOG +ISPS + Un_loading + CFS + Anti_Terror + Custom_clearance + Cargo_Service)

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
