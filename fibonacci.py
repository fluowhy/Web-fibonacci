# -*- coding: utf-8 -*-

from flask import Flask
from flask import request

# Este programa crea una web en localhost:5000 que permite ingresar un numero el cual corresponde a un termino de una sucesion de fibonacci y devuelve el termino n y n-1 de la sucesion.

def fibo(x):
	if x==0:
		return 0
	elif x==1:
		return 1
	else:
		return fibo(x-1) + fibo(x-2)

app = Flask(__name__)

@app.route('/')
def index():
 	return 
"""<!DOCTYPE html>
<html>
<body>
<h1>Sucesion de Fibonacci</h1>
<h2>Se retorna el elemento Sn y Sn-1 de la sucesion dado n.</h2>
<form action="." method="POST">
n=<input type="number" name="num">
<input type="submit" name="my-form" value="Send">
</form>
</body>
</html>"""

@app.route('/', methods=['POST'])
def my_form_post():
    	n = int(request.form['num'])	
	if n==0:
		return 'Termino unico: S_0=0'
	elif n==1:
		return 'S_1=1, S_0=0'
	else:
		return 'S_'+str(n)+'='+str(fibo(n))+', S_'+str(n-1)+'='+str(fibo(n-1))

if __name__ == '__main__':
   	app.run()

