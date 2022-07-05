def make_forecasts():
    """Construya los pronosticos con el modelo entrenado final.

    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:

    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.

    """
    import pandas as pd
    from Comun import DatosTrainTest
    from Comun import CargarDatos
    from Comun import CargarMejorModelo
    import shutil

    #copia el archivo de precios-diarios.csv en la carpeta features 
    shutil.copy('data_lake/business/precios-diarios.csv', 'data_lake/business/features/precios_diarios.csv')

    x, y = CargarDatos()
    Estimator = CargarMejorModelo()
    x_train, x_test, y_train, y_test = DatosTrainTest(x, y)
    y_pred = Estimator.predict(x)

    #Cargamos el archivo de precios diarios
    path_file = './data_lake/business/precios-diarios.csv'

    #Leemos el dataframe y le adicionamos la columna con los pronosticos
    datos = pd.read_csv(path_file, index_col=None, sep=',', header=1)
    datos['pronostico'] = y_pred
    datos.columns = ['Fecha', 'Precio promedio real de la electricidad', 'Pronóstico del precio promedio real']
    
    datos.to_csv('data_lake/business/forecasts/precios-diarios.csv', index=None)
    datos.to_csv('data_lake/business/forecasts-precios-diarios.csv', index=None)

    #raise NotImplementedError("Implementar esta función")
    
    if __name__ == "__main__":
        import doctest

        doctest.testmod()
        
        make_forecasts()
