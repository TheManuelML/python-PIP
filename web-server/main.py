import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1 ,2 ,3]

@app.get('/hyperblog', response_class=HTMLResponse)
def get_list():
    return '''
    <html>
        <head>
            <title>Hyperblog 2.0 es un blog del futuro</title>
        </head>
        <body>
            <div id="container">
                <div id='cabecera'>
                    Hyperblog
                    <span id="tagline">Tu blog de confianza</span>       
                </div>
                <div id="post">
                    <h1>Este es el t&iacute;tulo atractivo e interesante del post</h1>
                    <p>Y este es el p&aacute;rrafo de inicio donde vamos a explicar las cosas incre&iacute;bles que se pueden hacer con ramas</p>
                    <p>Los blogs son la mejor forma de compartir informaci&oacute;n y tus ideas. Mucho mas que ir a conferencias o salir en Youtube. Excepto si eres un rockstar. Pero estad&iacute;sticamente no lo eres.... por ahora.</p>
                    <p>Suscribete y dale like</p>         
                </div>
                <div id="footer">
                    Hecho con amor en Platzi &lt;3
                </div>
            </div>
        </body>
    </html>
    '''


def run():
    store.get_categories()

if __name__ == '__main__':
    run()