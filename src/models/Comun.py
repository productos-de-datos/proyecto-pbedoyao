""" 
    Se crean las funciones necesarias para entrenar y pronosticar
    el valor en pesos de Klb de energia
    
"""
import pandas as pd
import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def CargarDatos():
        
    Datos = pd.read_csv('./data_lake/business/features/precios_diarios.csv', sep=",")
    Datos['Fecha'] = pd.to_datetime(Datos['Fecha'], format='%Y-%m-%d')
    Datos['year'] = Datos['Fecha'].dt.year
    Datos['month'] = Datos['Fecha'].dt.month
    Datos['day'] = Datos['Fecha'].dt.day

    y = Datos["Precio"]
    x = Datos.copy()
    x.pop("Precio")
    x.pop("Fecha")
    return x, y

def DatosTrainTest(x, y):

    (x_train, x_test, y_train, y_test) = train_test_split(
        x,
        y,
        test_size=0.25,
        random_state=123456,
    )
    return x_train, x_test, y_train, y_test
 
def MejorModelo(estimator):

    if not os.path.exists("src/models/"):
        return None
    with open("src/models/precios-diarios.pickle", "wb") as file:
        pickle.dump(estimator, file)

def CargarMejorModelo():

    if not os.path.exists("src/models/"):
        return None
    with open("src/models/precios-diarios.pickle", "rb") as file:
        estimator = pickle.load(file)

    return estimator

def Evaluacion(y_true, y_pred): 
    
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    return mse, mae, r2


