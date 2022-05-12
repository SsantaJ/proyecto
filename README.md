# Pasos a seguir:

# 1. Nos aseguramos que tengamos el git instalado en nuestra maquina y ejecutamos el siguiente comando en el terminal:
git clone https://github.com/SsantaJ/proyecto.git

# 2. Despues ingresamos a la carpeta /proyecto y ejecutamos el siguiente comando (Asegurate de no tener ningun servicio en el puerto 80):
sudo docker build -t servermap:v01 .

# 3. Finalizamos ejecutando:
sudo docker run -d -p 80:80 servermap:v01 python3 app.py

# Ya con esto ya tenemos nuestro servidor montado, puedes verificar colocando "localhost" en tu navegador :)
