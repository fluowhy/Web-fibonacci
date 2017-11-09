# -*- coding: utf-8 -*-

from __future__ import division
import numpy as np
from flask import Flask
from flask import request

# Este programa crea una web en localhost:5000 que permite ingresar un numero el cual corresponde a un termino de una sucesion de fibonacci y devuelve el termino n y n-1 de la sucesion.
# Muestra si la entrada en la pagina es valida o no (error), tanto por inputs de un usuario de localhost:5000 o por el script test.py.

# funcion antigua, lenta
"""
def fibo(x):
	if x==0:
		return 0
	elif x==1:
		return 1
	else:
		return fibo(x-1) + fibo(x-2)
"""
# funcion nueva, rapida
def fibo(x):
	gold = (1 + np.sqrt(5))*0.5
	n_fibo = int(gold**x/np.sqrt(5)+0.5)
	return n_fibo
app = Flask(__name__)

@app.route('/')
def index():
 	return """<!DOCTYPE html>
<html>
<body>
<h1>Sucesion de Fibonacci</h1>
<h2>Se retorna el elemento Sn y Sn-1 de la sucesion dado n.</h2>
<form action="" method="POST">
n=<input type="number" name="num">
<input type="submit" name="my-form" value="Send">
</form>
</body>
</html>"""

@app.route('/', methods=['POST'])
def my_form_post():
	try:	
		n = request.form['num']		    	
		N = int(n)
		print 'Test:', n, 'No hubo error'	
		if N==0:
			return 'Termino unico: S_0=0'
		elif N==1:
			return 'S_1=1, S_0=0'
		else:
			return 'S_'+str(N)+'='+str(fibo(N))+', S_'+str(N-1)+'='+str(fibo(N-1))	
	except ValueError:
		print 'Test: ', n, 'ERROR'


if __name__ == '__main__':
   	app.run()

