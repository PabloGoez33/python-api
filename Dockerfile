# Indica la imagen base
FROM python:3.7.11-slim

# Establecer el directorio de trabajo
WORKDIR  /python-api

# Copiar el archivo de requisitos e instalar las dependencias
COPY requirements.txt requirements.txt

# Instalar las dependencias
RUN pip install -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Define el comando para ejecutar la aplicación
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
