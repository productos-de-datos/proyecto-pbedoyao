def train_daily_model():
    
    from Comun import CargarDatos
    from Comun import DatosTrainTest
    from Comun import MejorModelo
    from Comun import Evaluacion
    import numpy as np
    from sklearn.linear_model import ElasticNet
    from sklearn.model_selection import GridSearchCV
    

    alphas=np.linspace(0.0001, 0.5, 10)
    l1_ratios=np.linspace(0.0001, 0.5, 10)
    n_splits=5
    
    x, y = CargarDatos()
    x_train, x_test, y_train, y_test = DatosTrainTest(x, y)
    
    Estimator = GridSearchCV(
            ElasticNet(
            random_state=12345,
        ),
        param_grid={
            "alpha": alphas,
            "l1_ratio": l1_ratios,
        },
        cv=n_splits,
        refit=True,
        return_train_score=False,
    )

    Estimator.fit(x_train, y_train)

    y_pred=Estimator.predict(x_test)

    mse, mae, r2 = Evaluacion(y_test, y_pred)

    MejorModelo(Estimator)
   
    print(len(y_pred))
    #raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    
    train_daily_model()