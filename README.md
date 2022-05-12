# Pasos a seguir:

sudo apt-get update
sudo apt-get upgrade (s)
sudo apt-get install git (s)
git --version
sudo apt install docker.io (s)
sudo systemctl start docker
sudo systemctl enable docker
sudo systemctl status docker (Verificar funcionamiento)

sudo docker rm -f $(sudo docker ps -a -q)
sudo docker build -t servermap:v01 . (En la carpeta donde este el Dockerfile)
sudo docker run -d -p 80:80 servermap:v01 python3 app.py

# 1. Ejecutar el siguiente comando:
RUN git clone https://github.com/SsantaJ/proyecto.git
# 2. Ejecutar el siguiente:comando:
RUN sudo docker build -t servermap:v01 .
RUN sudo docker run -d -p 80:80 servermap:v01 python3 app.py
