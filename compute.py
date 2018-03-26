from numpy import exp, cos, linspace
import matplotlib.pyplot as plt
import os, time, glob
import pandas as pd
import math
import ast

def damped_vibrations(t, A, b, w):
	return A*exp(-b*t)*cos(w*t)

def compute(A, b, w, T, resolution=500):
	"""Return filename of plot of the damped_vibration function."""
	t = linspace(0, T, resolution+1)
	u = damped_vibrations(t, A, b, w)
	plt.figure()  # needed to avoid adding curves in plot
	plt.plot(t, u)
	plt.title('A=%g, b=%g, w=%g' % (A, b, w))
	if not os.path.isdir('static'):
		os.mkdir('static')
	else:
		# Remove old plot files
		for filename in glob.glob(os.path.join('static', '*.png')):
			os.remove(filename)
	# Use time since Jan 1, 1970 in filename in order make
	# a unique filename that the browser has not chached
	plotfile = os.path.join('static', str(time.time()) + '.png')
	plt.savefig(plotfile)
	return plotfile

## new func ##
def getCBM(l, w, h):
	return l*w*h

#in Germany		
def getPrePrice(PLZ,CBM,Weight):
	#xl=pd.ExcelFile("./price_table.xlsx")
	#df=xl.parse("pre")
	df=pd.read_excel("./static/price_table.xlsx","pre",header=[0,1]) #0:cbm; 1:height
	CBM,Weight=math.ceil(CBM),math.ceil(Weight)
	row=df.ix[df[('PLZ','bis')]>=PLZ].ix[df[('PLZ','von')]<=PLZ] #重量与体积975->1120
	#row1=
	CBM,Weight=math.ceil(CBM),math.ceil(Weight/50)*50
	price=row[(CBM,Weight)].iloc[0]	
	return math.ceil(price/50)*50
	
#in China	
def getPostPrice(Province, City, CBM, Weight):
	df=pd.read_excel("./static/price_table.xlsx","post",header=[0])
	#row=df.ix[df['Origin'].str.contains(r'Shanghai')==True]
	if City=='Others':	
		row=df.ix[df['Origin'].str.contains(r'Others in' + Province)==True]
	else:		
		row=df.ix[df['Origin'].str.contains(City)==True]

	Weight=max(CBM*250, Weight)
	if Weight>10000:
		s=row[10001].iloc[0]
	elif Weight>5000:
		s=row[5001].iloc[0]
	elif Weight>2000:
		s=row[2001].iloc[0]
	elif Weight>250:
		s=row[251].iloc[0]
	else:
		s=row[0].iloc[0] 
	#fn = ast.Lambda('Weight', s)	
	#return fn(w)
	print(s)
	price=eval(s)
	return math.ceil(price/50)*50
	
if __name__ == '__main__':
	print(compute(1, 0.1, 1, 20))