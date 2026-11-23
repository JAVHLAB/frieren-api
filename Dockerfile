# 1. Usamos una versión ligera de Python 3.11 (o la que uses)
FROM python:3.13 -slim

# 2. Creamos una carpeta de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiamos los requerimientos y los instalamos
# (Hacemos esto primero para aprovechar el caché de Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiamos todo el código de nuestro proyecto
COPY . .

# 5. Exponemos el puerto donde vivirá la API
EXPOSE 8000

# 6. El comando de encendido usando Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]