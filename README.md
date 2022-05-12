# Pasos a seguir:
# 1. Ejecutar el siguiente comando:
RUN git clone https://github.com/SsantaJ/proyecto.git
# 2. Ejecutar el siguiente:comando:
RUN sudo docker build -t servermap:v01 .
RUN sudo docker run -d -p 80:80 servermap:v01 python3 app.py
