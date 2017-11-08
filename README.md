# Web-fibonacci
El programa levanta una página web en localhost que permite calcular el término n y n-1 de una sucesión de Fibonacci.
# Antes de usar
Para la ejecución del programa se necesita intalar la librería Flask http://flask.pocoo.org, la cual permite la comunicación entre la web y el programa de python, y la librería Numpy http://www.numpy.org para cálculos numéricos. La aplicación fue probada con Python 2.7 por lo que existe la posibilidad de error de compatibilidad si se utiliza versiones actuales. 
# Cómo ejecutar el programa
La forma recomendada de ejecución es abriendo un terminal y ejecturar Python en él. Una vez abierto el programa se puede ejecutar el script fibonacci.py desde el terminal.
# Cómo utilizar la web
Si se realizaron los pasos anteriores, la forma de ingresar a la web es a través de localhost:5000. La dirección anterior debe ser escrita en la barra de direcciones de un browser a elección (único browser probado: Vivaldi). En ella se debe ingresar un numero entero y apretar el botón Send (o en su defecto la tecla Enter) para enviar la solicitud. Si se desea evaluar otra, se debe volver atrás y repetir el procedimiento.
# Créditos
Parte del código fue inspirado en https://stackoverflow.com/questions/12277933/send-data-from-a-textbox-into-flask, para luego realizar las modificaciones correspondientes dado el problema a solucionar. 
