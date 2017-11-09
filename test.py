# -*- coding: utf-8 -*-

import requests

# Este programa pone a prueba a fibonacci.py a traves de 9 entradas de distinto tipo (string, float, int) localhost puerto 5000, utilizado por fibonacci.py

pay = [1, 2, '3', '4', '', 1e-3, 'sdds', 1e3, "0,7"]

for i in pay:
	payload = {'num':i, 'my-form':'Send'}
	requests.post('http://localhost:5000', data=payload)

