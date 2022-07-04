def make_monthly_prices_plot():
    """Crea un grafico de lines que representa los precios promedios mensuales.
    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.
    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.
    """
    
    import pandas as pd
    import matplotlib.pyplot as plt

    precios_mensuales = pd.read_csv('data_lake/business/precios-mensuales.csv')

    fig, ax = plt.subplots()
    ax.plot(precios_mensuales['Fecha'], precios_mensuales['Precio'])
    plt.xlabel("Fecha")
    plt.ylabel("Precio")
    plt.title("Precio Promedio Mensual")
    plt.savefig('data_lake/business/reports/figures/monthly_prices.png')


    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    make_monthly_prices_plot()