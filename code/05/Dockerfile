#Descargamos la imagen base oficial para Python.
FROM python:3.9

# Establecemos el directorio de trabajo como /code.
#
#Acá serán ubicados el archivo requirements.txt y el directorio de la aplicación.
WORKDIR /code

#Copia el archivo con los requerimientos a la carpeta /code
#
#Como este archivo tiene una frecuencia de cambio baja, Docker usará una versión en caché de este para el siguiente paso. 
COPY ./requirements.txt /code/requirements.txt

# Instalar los paquetes de las dependencias mencionadas en el archivo de requerimientos.
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#Copia el directorio ./app dentro de la carpeta /code.
#
#Es importante realizar esta tarea casi al final del Dockerfile, para optimizar los tiempos de construcción de la imagen.
COPY ./app /code/app
CMD ["ls"]

# Ejecutar el comando para iniciar el servidor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
