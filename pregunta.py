"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import nltk
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";",
                     thousands=None,  # separador de miles para números
                     decimal=".",  # separador de decimales
                     )
    df=df.copy()
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x) #limpiar espacios en blancos
    df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x) # Convertir todos los datos a minúsculas
    df=df.drop_duplicates() #elimiar duplicados
    df=df.dropna()#eliminar filas vacias
    df.monto_del_credito=df.monto_del_credito.str.strip("$") #eliminar simbologia
    df.monto_del_credito=df.monto_del_credito.replace({',':''},regex=True).apply(pd.to_numeric) 
                  # para quitar el separador decimal y, a continuación, utiliza pd.to_numeric() 
                 #para convertir las columnas a tipo numérico. El resultado se muestra en la consola.
    df.comuna_ciudadano=df.comuna_ciudadano.astype(int)
    return df

print(clean_data())