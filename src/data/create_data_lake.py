def create_data_lake():
    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```
    """
    
    import os

    os.mkdir("data_lake")
    os.mkdir("data_lake/landing")
    os.mkdir("data_lake/raw")
    os.mkdir("data_lake/cleansed")
    os.mkdir("data_lake/business")
    os.mkdir("data_lake/business/reports")
    os.mkdir("data_lake/business/reports/figures")
    os.mkdir("data_lake/business/features")
    os.mkdir("data_lake/business/forecasts")
    
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    
    create_data_lake()
    
