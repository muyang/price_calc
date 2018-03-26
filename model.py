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

	