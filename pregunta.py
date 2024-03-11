"""

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import re
from unidecode import unidecode
from datetime import datetime
import pandas as pd
def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";",index_col=0)
    df=df.copy() 
    df=df.drop_duplicates() #elimiar duplicados
    df=df.dropna()#eliminar filas vacias
    df["sexo"] = df["sexo"].str.lower()  # Reemplazar todo por minuscula

    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].replace("-", " ").replace("_", " ").replace(". ", ".")

    df["idea_negocio"] = df["idea_negocio"].str.lower()  # Reemplazar todo por minuscula
    df["idea_negocio"] =[
        fila.replace("-", " ").replace("_", " ").replace(". ", ".")
        for fila in df["idea_negocio"]
    ]


   

    df["barrio"] = df["barrio"].str.lower().replace("antonio nari¿o", "antonio nari¿o").replace('bel¿n', "belen")
    df["barrio"] = df["barrio"].apply(lambda x: unidecode(x))
    df["barrio"] =[fila.replace("-", " ").replace("_", " ").replace(". ", ".") for fila in df["barrio"]]
    df["barrio"] = df["barrio"].str.strip()




    df["estrato"] = df["estrato"].astype(int)

    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)

    df["monto_del_credito"] = [
        fila.replace(".00", "").replace("$", "").replace(",", "").replace(".", "")
        for fila in df["monto_del_credito"]
    ]

    df["monto_del_credito"] = df["monto_del_credito"].astype(int)

    df["línea_credito"] = df["línea_credito"].str.lower().str.strip()
    df["línea_credito"] = [
        fila.replace("-", " ").replace("_", " ").replace(". ", ".")
        for fila in df["línea_credito"]
    ]

    # df["sexo"]=df["sexo"].str.lower() # Reemplazar todo por minuscula
    # df["tipo_de_emprendimiento"]=df["tipo_de_emprendimiento"].str.lower()
    
    # df["idea_negocio"]=df["idea_negocio"].str.lower()
    # df["idea_negocio"]=df["idea_negocio"].str.replace("_"," ").replace("-"," ")
    # df["idea_negocio"]=df["idea_negocio"].str.replace("-"," ")

    # df["barrio"]=df["barrio"].str.lower()
    # df["barrio"]=df["barrio"].str.replace("_"," ")
    # df["barrio"]=df["barrio"].str.replace("-"," ")
    # df["barrio"]=df["barrio"].str.strip()


#df[columna_fechas] = pd.to_datetime(df[columna_fechas], errors='coerce')
    df["fecha_de_beneficio"] = [
        (
            datetime.strptime(date, "%d/%m/%Y")
            if bool(re.search(r"\d{1,2}/\d{2}/\d{4}", date))
            else datetime.strptime(date, "%Y/%m/%d")
        )
        for date in df["fecha_de_beneficio"]
    ]




    #kw='belén'
    #df = df[df['barrio'].isin([kw])] #dejar solo los datos con esa palabra clave

    #kw=['mantenimiento-en-','mantenimiento-en-','distribuidora-de-','lavadero-de-','publicidad_y_','publicidad-y-','mantenimiento en ','publicidad y ','almacen_de_ropa_en_','distribuidora_de_'
    #     'organización_y_','venta de ','fabrica de ','fabrica-de-','deposito de ','almacen de ropa en ','fabrica_de_','lenceria para el ','lavadero de ','deposito_de_',
    #    'almacen-de-ropa-en-']
    #df = df[~df['idea_negocio'].str.contains('|'.join(kw))]
    # d1=(set(df["idea_negocio"].to_list()))
    # lista=list(df["idea_negocio"].value_counts())

   #df=df.drop_duplicates()
    #return set(list(df["barrio"]))
    return df["barrio"].value_counts()

   

print(clean_data())


