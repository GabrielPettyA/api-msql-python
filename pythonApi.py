#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 'requests' => librería que facilita las peticiones HTTP, sirve para realizar solicitudes HTTP.
import requests

# 'mysql.connector' => módulo de python que permite conectarte y comunicarte con BD. mysql.
import mysql.connector


# URL de la API
url = "https://rickandmortyapi.com/api/character/"

# Realizar la solicitud GET para traer los datos registrados en la URL.
# 'requests' es un paquete al cual se le puede hacer consultas de tipo 'HTTP'.
# 'get' sirve realizar una petición al sitio seleccionado.
response = requests.get(url)


# Verificar si la solicitud fue exitosa mediante codigo de estado de respuesta HTTP 200 
# De lo obtenido solo nos interesa el array results ya que es donde se encuentran los datos de los personajes. (status_code = código de estado de respuesta HTTP)
# .json => formato de datos basado en texto, sirve para transmitir datos a través de una red.
if response.status_code == 200: 
    data = response.json()["results"]
    
    
# Conectar a MySQL pasando los parámetros para poder realizarla.
# Se utiliza el método 'mysql.connector.connect()'
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    port = '3306'
)

# Se guarda en 'cursor' la conexión para poder ser llamada cuando se requiera.
# Se genera un objeto cursor el cual nos permite interactuar con BD. permitiendonos realizar
# consultas, insertar datos, actualizar registros, etc.
cursor = connection.cursor()
print("conexión a BD. en proceso...")

# Crear base de datos en caso de no existir.
cursor.execute("CREATE DATABASE IF NOT EXISTS api_python")
cursor.execute("USE api_python")
print("Base de Datos generada correctamente.")

# Crear tabla en caso de no existir con los campos referidos.
cursor.execute("""
CREATE TABLE IF NOT EXISTS datos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    status VARCHAR(255)
)
""")
print("Tabla 'datos' generada correctamente.")

 # Se realiza bucle for para obtener los datos del .json y poder registrarlo en la tabla 'datos'.
for char in data:
  id = char.get('id')
  name = char.get('name')
  status = char.get('status')
  
  # Se ingresan la información obtenida en el bucle en la tabla 'datos'.
  sql = "INSERT INTO datos (name, status) VALUES (%s, %s)"
  datosChar = (name, status)
  cursor.execute(sql, datosChar)
  

# verifica la correcta ejecución de los cambios solicitados.
connection.commit()
print("Inserción de Datos exitoso !!!")
# Cerrar la conexión y el cursor.
cursor.close()
connection.close()

