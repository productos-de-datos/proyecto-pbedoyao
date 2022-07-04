def make_daily_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

    """
  
    import pandas as pd
    import matplotlib.pyplot as plt

    precios_diarios = pd.read_csv('data_lake/business/precios-diarios.csv')

    fig, ax = plt.subplots()
    ax.plot(precios_diarios['Fecha'], precios_diarios['Precio'])
    plt.xlabel("Fecha")
    plt.ylabel("Precio")
    plt.title("Precio Promedio Diario")
    plt.savefig('data_lake/business/reports/figures/daily_prices.png')
    
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    make_daily_prices_plot()
