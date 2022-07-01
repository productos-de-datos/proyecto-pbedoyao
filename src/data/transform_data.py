def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    import sys
    from datetime import datetime
    from os import remove
    import pandas as pd
    import os

    ArchivosLanding = []
    for Archivo in os.listdir("data_lake/landing/"):
        if Archivo.endswith(".xls") or Archivo.endswith(".xlsx"):
            ArchivosLanding.append(Archivo) 
    
    
    for Archivos in ArchivosLanding:
        try:            
            dfArchivo = pd.read_excel("data_lake/landing/" + Archivos)
            
            if dfArchivo.columns[0] != "Fecha":
                FilaInicianDatos = dfArchivo[dfArchivo.iloc[:, 0] == "Fecha"].index[0] + 1
                dfArchivo = pd.read_excel("data_lake/landing/" + Archivos, skiprows=FilaInicianDatos)
                NombreArchivo = Archivos.split("/")[-1]
                NombreArchivoCSV = NombreArchivo.split(".")[0] + ".csv"
                dfArchivo.to_csv("data_lake/raw/" + NombreArchivoCSV, index=False) 
            else:
                NombreArchivo = Archivos.split("/")[-1]
                NombreArchivoCSV = NombreArchivo.split(".")[0] + ".csv"
                dfArchivo.to_csv("data_lake/raw/" + NombreArchivoCSV, index=False) 
        except:
            print("Error al transformar el archivo " + Archivos )
        
    
    #raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":  
    import doctest

    doctest.testmod()
    
    transform_data()