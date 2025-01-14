Proyecto Urban Routes
Andrea Salcedo Morales, grupo 18, Sprint 8. Automatización de pruebas de la aplicación web
-Descripción del proyecto: comprobación de la funcionalidad de la aplicación Urban Routes con pruebas automatizadas del proceso de pedir un taxi con la tarifa comfort y otras especificaciones del viaje. Entre las funcionalidades a incluir están rellenar el campo de número de teléfono, agregar una tarjeta bancaria, escribir un mensaje para el conductor; solicitar manta, pañuelos y helado.

-Tecnologías utilizadas e instalación: 

*Python 
Se descarga en https://www.python.org/downloads/
*PyCharm 
El link de descarga es https://www.jetbrains.com/pycharm/download/?section=windows#section=windows
*Pytest 
Existen dos métodos para instalar Pytest: 1️⃣ Usando el comando "pip" en la terminal: En la terminal/consola se ingresa el comando "pip install pytest" (o "pip3", si "pip" no funciona). 2️⃣ En PyCharm en la pestaña "Python Packages": En el proyecto de PyCharm en el panel inferior seleccionar la pestaña "Python Packages". Introducir "Pytest" en el campo de búsqueda. Luego seleccionar el paquete "Pytest" de la lista y hacer clic en el botón "Install".
*Selenium Webdriver.Chrome
*Selenium Keys
*Selenium By
*Selenium expected_conditions
*Selenium WebDriverWait
En relación con Selenium este se instala en la terminal/consola ingresando el comando "pip install selenium" (o "pip3", si "pip" no funciona)
*HTML

-Ejecución de pruebas 
Desde la terminal de PyCharm En la pestaña "Terminal" en la parte inferior de PyCharm para ejecutar todas las pruebas del proyecto se escribe: pytest Luego ejecuta las pruebas desde el archivo main.py con: pytest main.py
