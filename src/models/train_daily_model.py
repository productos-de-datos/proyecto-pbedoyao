def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl
    
    """
        
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.ensemble import RandomForestRegressor
    import pickle

    def ObtenerDatos(data):
        
        Datos = pd.read_csv('data_lake/business/features/precios_diarios.csv', sep=",")
        Datos['fecha'] = pd.to_datetime(Datos['fecha'], format='%Y-%m-%d')
        Datos['year'] = Datos['fecha'].dt.year
        Datos['month'] = Datos['fecha'].dt.month
        Datos['day'] = Datos['fecha'].dt.day

        y = Datos["precio"]
        x = Datos.copy()
        x.pop("precio")
        x.pop("fecha")
        return x, y

    def make_train_test_split(x, y):

        (x_train, x_test, y_train, y_test) = train_test_split(
            x,
            y,
            test_size=0.30,
            random_state=12345,
        )
        return x_train, x_test, y_train, y_test

    def train_mode(x_train, x_test):

        scaler = StandardScaler()
        scaler.fit(x_train)
        x_train = scaler.transform(x_train)
        x_test = scaler.transform(x_test)

        model_RF = RandomForestRegressor(n_jobs=-1)
        
        return model_RF

    def SalvarModelo(model_RF):

        with open("src/models/precios-diarios.pickle", "wb") as file:
            pickle.dump(model_RF, file,  pickle.HIGHEST_PROTOCOL)

    def train_daily_model():
        
        data = pd.read_csv('data_lake/business/features/precios_diarios.csv', sep=",")
        x, y = ObtenerDatos(data)
        x_train, x_test, y_train, y_test = make_train_test_split(x, y)
        model_RF = train_mode(x_train, x_test)
        SalvarModelo(model_RF)

        #raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    
    train_daily_model()
