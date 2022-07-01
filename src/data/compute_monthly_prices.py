def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional

    """
    #raise NotImplementedError("Implementar esta función")
    
    import pandas as pd

    Datos = pd.read_csv('./data_lake/cleansed/precios-horarios.csv')
    Datos["Fecha"] = pd.to_datetime(Datos["Fecha"], format='%Y-%m-%d').dt.to_period("M").dt.to_timestamp()
    DatosAgrupados = Datos.groupby(by="Fecha",as_index=False).agg({"Precio":"mean"})
    DatosAgrupados.to_csv('./data_lake/business/precios-mensuales.csv', encoding='utf-8', index=False)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    
    compute_monthly_prices()
