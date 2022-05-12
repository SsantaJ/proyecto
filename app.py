#llamar librerias
from dash import Dash, html, dcc  #libreria para servidor web de data science

#declarar objetos principales
app = Dash(__name__)

#configurar el sitio web
app.layout = html.Div([html.H1('Programa de Samuel Santa'),
                       html.Div('BLA BLA BLA BLA BLA BLA BLA...')])
#funcion principal
if __name__ == '__main__':
    #cargar el objeto principal a todas las interfaces de red en el puerto 80
    app.run_server(host='0.0.0.0',port=80)
