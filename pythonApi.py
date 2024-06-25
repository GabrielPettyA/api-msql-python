import requests
import mysql.connector


# URL de la API
url = "https://rickandmortyapi.com/api/character/"

# Realizar la solicitud GET para traer los datos registrados en la URL.
response = requests.get(url)

# Verificar si la solicitud fue exitosa mediante codigo igualado a 200 
# de lo obtenido solo nos interesa el array results ya que es donde se encuentran los datos de los personaes.
if response.status_code == 200: 
    data = response.json()["results"]
    
    
# Conectar a MySQL pasando los parámetros para poder realizarla.
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    port = '3306'
)

# Se guarda en 'cursor' la conexión para poder ser llamada cuando se requiera.
cursor = connection.cursor()

# Crear base de datos en caso de no existir.
cursor.execute("CREATE DATABASE IF NOT EXISTS api_python")
cursor.execute("USE api_python")

# Crear tabla en caso de no existir con los campos referidos.
cursor.execute("""
CREATE TABLE IF NOT EXISTS datos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    status VARCHAR(255)
)
""")
 # Se realiza bucle for para obtener los datos del .json y poder registrarlo en la tabla 'datos'.
for char in data:
  id = char.get('id')
  name = char.get('name')
  status = char.get('status')
  
  # Se ingresan la información obtenida en el bucle en la tabla 'datos'.
  sql = "INSERT INTO datos (id, name, status) VALUES (%s, %s, %s)"
  datosChar = (id, name, status)
  cursor.execute(sql, datosChar)

# verifica la correcta ejecución de los cambios solicitados.
connection.commit()

# Cerrar la conexión y el cursor.
cursor.close()
connection.close()

