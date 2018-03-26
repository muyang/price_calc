from wtforms import Form, FloatField, validators, StringField
#from wtforms.validators import DataRequired, Email

from math import pi

class InputForm(Form):
	'''
	A = FloatField(
		label='amplitude (m)', default=1.0,
		validators=[validators.InputRequired()])
	b = FloatField(
		label='damping factor (kg/s)', default=0.3,
		validators=[validators.InputRequired()])

	w = FloatField(
		label='frequency (1/s)', default=2*pi,
		validators=[validators.InputRequired()])
	T = FloatField(
		label='validaton time (days)', default=120,
		validators=[validators.InputRequired()])
	'''		
	l = FloatField(
		label='length (m)', default=1.2,
		validators=[validators.InputRequired()])
	w = FloatField(
		label='width (m)', default=0.8,
		validators=[validators.InputRequired()])
	h = FloatField(
		label='height (m)', default=4.8,
		validators=[validators.InputRequired()])
	Weight = FloatField(
		label='weight (kg)', default=975,
		validators=[validators.InputRequired()])
	PLZ = FloatField(
		label='postcode (01000~97900)', default=84168,
		validators=[validators.InputRequired()])
		
	Province = StringField('Province (Jiangsu, Beijing)', default='Jiangsu', validators=[validators.DataRequired()])
	City = StringField('City (Suzhou, Beijing)', default='Taizhou', validators=[validators.DataRequired()])

	FOG = FloatField(
		label='FOG price per CBM:€/cbm', default=120,
		validators=[validators.InputRequired()])	
	ISPS = FloatField(
		label='ISPS price:€', default=2.5,
		validators=[validators.InputRequired()])
	Un_loading = FloatField(
		label='loading or unloading fee:€/kg', default=31.5/1000,
		validators=[validators.InputRequired()])		

	CFS = FloatField(
		label='CFS fee per CBM:€/cbm', default=12,
		validators=[validators.InputRequired()])
	Terror = FloatField(
		label='anti-terror service fee:€', default=3,
		validators=[validators.InputRequired()])
	Cargo = FloatField(
		label='Cargo Service fee:€', default=7,
		validators=[validators.InputRequired()])
	Custom = FloatField(
		label='Cargo Service fee(RMB：¥)', default=300,
		validators=[validators.InputRequired()])
	eu2us = FloatField(
		label='€/$ ', default=1.15,
		validators=[validators.InputRequired()])
	us2rmb = FloatField(
		label='$/¥', default=6.5,
		validators=[validators.InputRequired()])