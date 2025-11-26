
# Importamos variables
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
app = FastAPI()

# 
# Hay que activar el entorno e irnos a la carpeta donde este ubicado el archivo .py.
# Despues, instalar los pip necesarios (fastapi y uvicorn)
# Ponemos en la terminal el comando "uvicorn nombre_archivo:nombre_vinculado_FastAPI" --reload para 
# activar la api y podamos verla en el navegador.
# 
#

# Creamos app de saludo
@app.get("/api")
def hello(name = None):

    if name is None:
        text = 'Hola buenass! ' \
        'Por favor, registrese.'
    else:
        text = 'Bienvenido ' + name + ' a mi mundo. Te esperan unas divertidas clases de Python.'

    return text

# Creamos app que muestre contenido de un CSV
@app.get("/get-iris")
def get_iris():

    import pandas as pd
    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)

    return iris

# Creamos grafico con el contenido de un CSV
@app.get("/plot-iris")
def plot_iris():

    import pandas as pd
    import matplotlib.pyplot as plt

    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)

    plt.scatter(iris['sepal_length'], iris['sepal_width'])
    plt.savefig('iris.png')
    file = open('iris.png', mode="rb")

    return StreamingResponse(file, media_type="image/png")

