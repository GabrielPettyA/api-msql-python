# Desarrollo Sobre Redes        

- Se obtiene la URL a implementar para obtención de datos,
- Generación de Base de Datos y Tabla en MYsql,
- Lectura de datos de URL y manejo de información mediante '.json()',
- Carga de datos en la BD,
- Cierre de cursor y conexión. 


## API Reference

#### Get all items

```http
  GET /api/items
```

| program   | import   | Description                |
| :-------- | :------- | :------------------------- |
| `python`  | `requests`,`mysql.connector` | **Required**. URL. MySql|

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`,`name`,`status`      | `string` | **Required**. ID del elemento que se va a obtener de la Api. |

#### add(id, name, status)

Tomo tres datos de los elementos registrados en la URL.


                        
## Author:

- Pettinari Gabriel Alejandro
- [@Gabriel Pettinari](https://github.com/GabrielPetty)


