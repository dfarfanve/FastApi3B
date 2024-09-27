
# 🚀 Empezamos
![uvicorn](https://www.uvicorn.org/uvicorn.png)

Prueba Técnica | Tiendas 3B

“Programador Backend”
## 🔖 **Como iniciar**


`# FastAPI Product Inventory API

Esta es una aplicación de API REST desarrollada con FastAPI para gestionar productos, inventarios y órdenes de compra. La aplicación utiliza SQLite como base de datos y SQLModel para la gestión de modelos.

## Requisitos

- Python 3.7 o superior
- Docker (opcional, para ejecutar la aplicación en un contenedor)

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```
### 2. Crear un entorno virtual y activar

```bash
python -m venv env
source env/bin/activate
``` 

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Ejecución de la Aplicación

### 1. Correr la aplicación con Uvicorn

Puedes levantar el servidor de FastAPI utilizando Uvicorn:

```bash
`uvicorn main:app` 
```
El servidor estará disponible en `http://127.0.0.1:8000`.

Al iniciar la aplicación se inicia también el job, en segundo plano,  con una validación cada 60 segundos, se debe verificar en la consola el mensaje:
```bash
Product {product name} has low stock: {quantity}
```
### 2. Uso de Docker (Opcional)

Si prefieres ejecutar la aplicación dentro de un contenedor Docker, sigue los siguientes pasos:

#### Construir la imagen de Docker

```bash
`docker build -t fastapi-product-api .` 
```
#### Ejecutar el contenedor

```bash
`docker run -d -p 8000:8000 fastapi-product-api` 
```

Ahora la API estará disponible en `http://127.0.0.1:8000`.

## Endpoints Disponibles

- ``[POST] /api/products/`` - Create Product
- ``[PATCH] /api/inventories/product/{product_id}`` - Update Stock
- ``[POST] /api/orders/`` - Create Order


### Crear un producto

-   **URL:** `/api/products/`
-   **Método:** `POST`
-   **Cuerpo de la solicitud:**

   ```json 
    {
      "sku": "ABC123",
      "name": "New Product"
    }
  ```  

### Agregar stock a un producto

-   **URL:** `/api/inventories/product/{product_id}`
-   **Método:** `PATCH`
-   **Parámetros de consulta:**
    -   `product_id`: El id de producto que se desea aumentar el stock
-   **Cuerpo de la solicitud:**
 ``` json
    {
	"stock": 10
	}
```

### Crear una orden

-   **URL:** `/api/orders/`
-   **Método:** `POST`
-   **Cuerpo de la solicitud:**

 ``` json
    {
	"product_id": 1,
	"quantity": 5
	}
```    

## Documentación de la API


###  Documentación Interactiva

Ir a la dirección <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank">http://127.0.0.1:8000/docs</a>.

Al acceder, se puede ver la documentación que  proporcionado <a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a>

### Documentación Alternativa

Ir al enlace <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://127.0.0.1:8000/redoc</a>.

Se mostrará la documentación alternativa de  <a href="https://github.com/Rebilly/ReDoc" class="external-link" target="_blank">ReDoc</a>

### Nota adicional:
El archivo collection de postman se encuentra en la carpeta resources del repositorio
