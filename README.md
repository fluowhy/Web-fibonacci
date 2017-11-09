# Web-fibonacci
El programa levanta una página web en localhost que permite calcular el término n y n-1 de una sucesión de Fibonacci. Además se tiene un test para distintos tipos de entradas.
# Antes de usar
Para la ejecución del programa se necesita intalar la librería Flask http://flask.pocoo.org, la cual permite la comunicación entre la web y el programa de python, y la librería Numpy http://www.numpy.org para cálculos numéricos. El programa test.py utiliza la librería requests http://docs.python-requests.org/en/master/.
La aplicación fue probada con Python 2.7 por lo que existe la posibilidad de error de compatibilidad si se utiliza versiones actuales. 
# Cómo ejecutar fibonacci.py
La forma recomendada de ejecución es abriendo un terminal y ejecturar Python en él. Una vez abierto el programa se puede ejecutar el script fibonacci.py desde el terminal escribiendo run fibonacci.py.
# Cómo utilizar la web
Si se realizaron los pasos anteriores, la forma de ingresar a la web es a través de localhost:5000. La dirección anterior debe ser escrita en la barra de direcciones de un browser a elección (único browser probado: Vivaldi). En ella se debe ingresar un numero entero y apretar el botón Send (o en su defecto la tecla Enter) para enviar la solicitud. Si se desea evaluar otra, se debe volver atrás y repetir el procedimiento.
# Cómo ejecutar test.py
Abrir un segundo terminal con Python y escribir test.py. En el primer terminal se despliega la respuesta a la entrada de los tests, es decir, se informa si ésta fue errónea o no y la entrada correspondiente. 
# Créditos
Parte del código fue inspirado en https://stackoverflow.com/questions/12277933/send-data-from-a-textbox-into-flask, para luego realizar las modificaciones correspondientes dado el problema a solucionar. 
La forma cerrada para los términos de la sucesión de fibonacci fue obtenida de https://en.wikipedia.org/wiki/Fibonacci_number, sección Closed-form expression.
