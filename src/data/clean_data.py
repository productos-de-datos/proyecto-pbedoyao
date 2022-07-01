def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


    """
    #raise NotImplementedError("Implementar esta función")

    import pandas as pd
    from os import remove
    import os

    ArchivosRaw = []
    for Archivo in os.listdir("data_lake/raw/"):
        if Archivo.endswith(".csv"):
            ArchivosRaw.append(Archivo)

    for Archivo in ArchivosRaw:
        Data = pd.read_csv("data_lake/raw/" + Archivo)
        Data.dropna(subset=["Fecha"], inplace=True)
        Data["Fecha"] = pd.to_datetime(Data["Fecha"])
        Data["Fecha"] = Data["Fecha"].apply(lambda x: x.strftime("%Y-%m-%d"))
        NombreArchivo = Archivo.split("/")[-1]
        NumeroColumnas = len(Data.columns)

        if NumeroColumnas > 25:
            ColumnasABorrar = list(range(25, NumeroColumnas))
            Data = Data.drop(Data.columns[ColumnasABorrar], axis=1)

        Data.columns = ["Fecha","H00","H01","H02","H03","H04","H05","H06","H07","H08","H09","H10","H11","H12","H13","H14","H15","H16","H17","H18","H19","H20","H21","H22","H23",]

        remove("data_lake/raw/" + Archivo)
        Data.to_csv("data_lake/raw/" + NombreArchivo, sep=",", decimal=".", encoding="utf-8", index=False,)
            
    TodosArchivosCSV = []

    for ArchivoCSV in ArchivosRaw:
        Data = pd.read_csv(ArchivoCSV)
        Data = Data.fillna(method="bfill", axis=1)
        Data = pd.melt(Data, id_vars=["Fecha"], value_vars=["H00","H01","H02","H03","H04","H05","H06","H07","H08","H09","H10","H11","H12","H13","H14","H15","H16","H17","H18","H19","H20","H21","H22","H23",],)
        Data.columns = ["Fecha", "Hora", "Precio"]
        Data = Data.sort_values(by=["Fecha", "Hora"])

        TodosArchivosCSV.append(Data)

    ContenidoCSV = pd.concat(TodosArchivosCSV, ignore_index=True)
    ContenidoCSV.to_csv("data_lake/cleansed/precios-horarios.csv", index=False)

if __name__ == "__main__":
    import doctest

    doctest.testmod()

    clean_data()