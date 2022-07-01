"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------

"""


def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """
    
    import urllib.request as request
    import datetime as datetime
    import logging
    from os import remove

    FechaActula = datetime.datetime.now()
    AnoActual = FechaActula.year - 1995
    LisAno = list(range(1995, 1995 + AnoActual))
    
    def DescargarArchivo(Ano, Extension='xlsx'):
        Ano = str(Ano)
        try:
            ArchivoLocal = open(f"data_lake/landing/" + Ano + "." + Extension, "wb")
            ArchivoLocal.write(request.urlopen(f"https://github.com/jdvelasq/datalabs/raw/master/datasets/precio_bolsa_nacional/xls/" + Ano + "." + Extension).read())
            ArchivoLocal.close()
        except Exception:
            ArchivoLocal.close()
            if "data_lake/landing/" + Ano + ".xlsx":
                remove(f"data_lake/landing/" + Ano + ".xlsx")
            Extension='xls'
            ArchivoLocal = open(f"data_lake/landing/" + Ano + "." + Extension, "wb")
            ArchivoLocal.write(request.urlopen(f"https://github.com/jdvelasq/datalabs/raw/master/datasets/precio_bolsa_nacional/xls/" + Ano + "." + Extension).read())
            ArchivoLocal.close()
        except:
            logging.exception("Hubo un error descargando archivo del año: " & Ano)
    
    for Anos in LisAno:
        Anos = str(Anos)
        DescargarArchivo(Anos)
    
    raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
        
    ingest_data()
