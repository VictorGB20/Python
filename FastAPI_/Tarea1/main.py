
# Importamos variables
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
# app = FastAPI()

# # 
# # Hay que activar el entorno e irnos a la carpeta donde este ubicado el archivo .py.
# # Despues, instalar los pip necesarios (fastapi y uvicorn)
# # Ponemos en la terminal el comando "uvicorn nombre_archivo:nombre_vinculado_FastAPI" --reload para 
# # activar la api y podamos verla en el navegador.
# # 
# #

# # Creamos app de saludo
# @app.get("/api")
# def hello(name = None):

#     if name is None:
#         text = 'Hola buenass!\n ' \
#         'Por favor, registrese.'
#     else:
#         text = 'Bienvenido ' + name + ' a mi mundo.\n Te esperan unas divertidas clases de Python.'

#     return text

# # Creamos app que muestre contenido de un CSV
# @app.get("/get-iris")
# def get_iris():

#     url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
#     iris = pd.read_csv(url)

#     return iris

import pandas as pd
from fastapi import FastAPI, HTTPException, Query


iesazarquiel = FastAPI()

# Intentamos cargar el CSV al iniciar el módulo. Si falla, `df` será un DataFrame vacío.
try:
    df = pd.read_csv("./datos_alumnos.csv", sep=";", encoding="latin-1")
except Exception as e:
    print(f"Error al leer el CSV: {e}")
    df = pd.DataFrame()


def _get_alumno(codigoId: int):
    """Devuelve la fila del alumno como Series o lanza HTTPException si no existe."""
    if df.empty:
        raise HTTPException(status_code=503, detail="Datos no cargados (CSV no disponible).")
    alumno = df[df['ID'] == codigoId]
    if alumno.empty:
        raise HTTPException(status_code=404, detail=f"No se encontró ningún alumno con el ID {codigoId}")
    return alumno.iloc[0]


@iesazarquiel.get("/info-alumnos")
def info():
    """Devuelve lista de IDs disponibles."""
    if df.empty:
        raise HTTPException(status_code=503, detail="Datos no cargados (CSV no disponible).")
    return {"ids_disponibles": df['ID'].tolist()}


@iesazarquiel.get("/asistencia")
def asistencia(codigoId: int | None = Query(None, description="ID del alumno")):
    """Devuelve nombre, apellidos y asistencia de un alumno por su ID."""
    if codigoId is None:
        raise HTTPException(status_code=400, detail="Se requiere el parámetro 'codigoId'. Uso: /asistencia?codigoId=1001")
    datos = _get_alumno(codigoId)
    return {
        "nombre": datos.get('Nombre', 'Desconocido'),
        "apellidos": datos.get('Apellidos', 'Desconocido'),
        "asistencia": datos.get('Asistencia', None)
    }


@iesazarquiel.get("/notas")
def notas(codigoId: int | None = Query(None, description="ID del alumno"), notaConsultada: str | None = Query(None, description="Nombre de la columna de nota (opcional)")):
    """Si `notaConsultada` se proporciona devuelve esa nota; si no, devuelve todas las notas del alumno."""
    if codigoId is None:
        raise HTTPException(status_code=400, detail="Se requiere el parámetro 'codigoId'. Uso: /notas?codigoId=1001")
    datos = _get_alumno(codigoId)

    # Columnas que consideramos metadatos, no notas
    meta = {'ID', 'Nombre', 'Apellidos', 'Asistencia'}
    notas_cols = [c for c in df.columns if c not in meta]

    if notaConsultada:
        if notaConsultada not in df.columns:
            raise HTTPException(status_code=400, detail={
                "error": f"La categoría '{notaConsultada}' no existe.",
                "categorias_disponibles": notas_cols
            })
        return {
            "nombre": datos.get('Nombre'),
            "apellidos": datos.get('Apellidos'),
            "calificacion": {"modulo": notaConsultada, "nota": datos[notaConsultada]}
        }

    # Si no se pasa `notaConsultada`, devolvemos todas las notas disponibles
    todas_notas = {col: datos[col] for col in notas_cols}
    return {
        "nombre": datos.get('Nombre'),
        "apellidos": datos.get('Apellidos'),
        "notas": todas_notas
    }
    

    
