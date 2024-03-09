"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import nltk
import pandas as pd
def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df=df.copy()  
    df["sexo"]=df["sexo"].str.strip() # me borra espacios en blanco inicio-final
    df["sexo"]=df["sexo"].str.lower() # Reemplazar todo por minuscula
    df["sexo"]=df["sexo"].str.replace("_","") # Reemplazar todo por minuscula
    df["sexo"]=df["sexo"].str.lower() # Reemplazar todo por minuscula
    df["sexo"] = df["sexo"].str.translate(
        str.maketrans("", "", "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")) # revisar notas al respecto
    df["sexo"]=df["sexo"].str.split()
    stemmer = nltk.PorterStemmer()
    df["sexo"] = df["sexo"].apply(lambda x: [stemmer.stem(word) for word in x])
    df["sexo"] = df["sexo"].apply(lambda x: sorted(set(x)))  # set un conjunto que no se repiten elementos
    # sorted ordena 
    df["sexo"]=df["sexo"].str.join(" ") # me uno los dos strings de la lista.

    return df

print(clean_data())