import requests
import pandas as pd

#Funcion para consultar los indicadores del INPC en INEGI
def consultar_inpc():
    token ="bbd9c2b3-ecdf-a9dd-1632-0339fbb1d393"
    endpoint=  f"https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/910394,910395,910397,910398,910392/es/0/false/BIE-BISE/2.0/{token}?type=json"
    response= requests.get(endpoint,timeout=30)
    if response.status_code ==200:
        data = response.json()
        datos=[]
        #Recorrer las serie y sus observaciones
        for serie in data["Series"]:
            for observacion in serie["OBSERVATIONS"]:
                datos.append({
                    "Indicador": serie["INDICADOR"],
                    "Periodo": observacion["TIME_PERIOD"],
                    "Valor":observacion["OBS_VALUE"]
                })
        df =pd.DataFrame(datos)
        #Filtrar los registros del periodo 2000 a 2024
        df=df[(df["Periodo"].str[:4].astype(int) >= 2000)&(df["Periodo"].str[:4].astype(int)<= 2024)]
        #Convertir los valores a numeros decimales
        df["Valor"] = df["Valor"].astype(float)
        # Reiniciar los indices
        df.reset_index(inplace=True, drop=True)

        print("\nDatos del INPC")
        print(df.dtypes)
        print(df.head())
        print(df.tail())
        print("Cantidad de registros:", len(df))
        #Guardar los datos en un archivo CSV
        df.to_csv("Inpc_Inegi.csv",index=False, encoding="utf-8-sig")
    else:
        print("Error al consultar el INPC:", response.status_code)

#Funcion para consultar los nacimientos registrados en INEGI
def consultar_nacimientos():
    token ="bbd9c2b3-ecdf-a9dd-1632-0339fbb1d393"
    endpoint= f"https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/1002000026/es/0/false/BISE/2.0/{token}?type=json"
    response= requests.get(endpoint, timeout=30)
    if response.status_code ==200:
        data= response.json()
        datos =[]
        # Recorrer las series y sus observaciones
        for serie in data["Series"]:
            for observacion in serie["OBSERVATIONS"]:
                # Seleccionar los datos de cobertura nacional
                if observacion["COBER_GEO"] =="0":
                    datos.append({
                        "Indicador": serie["INDICADOR"],
                        "Periodo":observacion["TIME_PERIOD"],
                        "Valor": observacion["OBS_VALUE"]
                    })
        df =  pd.DataFrame(datos)
        #Filtrar los registros del periodo 2000 a 2024
        df=df[(df["Periodo"].astype(int) >= 2000) &(df["Periodo"].astype(int) <= 2024)]
        # Convertir los valores a numeros decimales
        df["Valor"] =df["Valor"].astype(float)
        #Reiniciar los indices
        df.reset_index(inplace=True, drop=True)

        print("\nDatos de nacimientos")
        print(df.dtypes)
        print(df.head())
        print(df.tail())
        print("Cantidad de registros:", len(df))
        #Guardar los datos en un archivo CSV
        df.to_csv("Nacimientos_Inegi.csv", index=False, encoding="utf-8-sig")
    else:
        print("Error al consultar los nacimientos:", response.status_code)

#Funcion para consultar la tasa global de fecundidad en Banco Mundial
def consultar_fecundidad():
    endpoint ="https://api.worldbank.org/v2/country/MEX/indicator/SP.DYN.TFRT.IN?date=2000:2024&format=json&per_page=100"
    response=requests.get(endpoint,timeout=30)
    if response.status_code== 200:
        data= response.json()
        datos =[]
        #Recorrer las observaciones obtenidas
        for observacion in data[1]:
            datos.append({
                "Indicador":observacion["indicator"]["id"],
                "Periodo":observacion["date"],
                "Valor": observacion["value"]
            })
        df=pd.DataFrame(datos)
        #Filtrar los registros del periodo 2000 a 2024
        df =df[(df["Periodo"].astype(int) >=2000) &(df["Periodo"].astype(int)<=2024)]
        # Convertir los valores a numeros decimales
        df["Valor"] = df["Valor"].astype(float)
        #Reiniciar los indices
        df.reset_index(inplace=True, drop=True)

        print("\nDatos de fecundidad")
        print(df.dtypes)
        print(df.head())
        print(df.tail())
        print("Cantidad de registros:", len(df))
        # Guardar los datos en un archivo CSV
        df.to_csv("Fecundidad_Bm.csv", index=False,encoding="utf-8-sig")
    else:
        print("Error al consultar la fecundidad:",response.status_code)

# Funcion para consultar el consumo de los hogares en moneda constante
def consultar_consumo():
    endpoint="https://api.worldbank.org/v2/country/MEX/indicator/NE.CON.PRVT.KN?date=2000:2024&format=json&per_page=100"
    response =requests.get(endpoint, timeout=30)
    if response.status_code ==200:
        data= response.json()
        datos = []
        # Recorrer las observaciones obtenidas
        for observacion in data[1]:
            datos.append({
                "Indicador": observacion["indicator"]["id"],
                "Periodo": observacion["date"],
                "Valor":observacion["value"]
            })
        df = pd.DataFrame(datos)
        # Filtrar los registros del periodo 2000 a 2024
        df = df[(df["Periodo"].astype(int) >= 2000) & (df["Periodo"].astype(int) <= 2024)]
        #Convertir los valores a numeros decimales
        df["Valor"] = df["Valor"].astype(float)
        #Reiniciar los indices
        df.reset_index(inplace=True, drop=True)
        print("\nDatos de consumo")
        print(df.dtypes)
        print(df.head())
        print(df.tail())
        print("Cantidad de registros:", len(df))
        #Guardar los datos en un archivo CSV
        df.to_csv("Consumo_Bm.csv", index=False, encoding="utf-8-sig")
    else:
        print("Error al consultar el consumo:", response.status_code)

#Funcion para consultar el crecimiento anual del consumo
def consultar_crecimiento_consumo():
    endpoint=  "https://api.worldbank.org/v2/country/MEX/indicator/NE.CON.PRVT.KD.ZG?date=2000:2024&format=json&per_page=100"
    response =requests.get(endpoint, timeout=30)
    if response.status_code==200:
        data=response.json()
        datos= []
        #Recorrer las observaciones obtenidas
        for observacion in data[1]:
            datos.append({
                "Indicador":observacion["indicator"]["id"],
                "Periodo":observacion["date"],
                "Valor": observacion["value"]
            })
        df =pd.DataFrame(datos)
        #Filtrar los registros del periodo 2000 a 2024
        df=df[(df["Periodo"].astype(int)>= 2000) &(df["Periodo"].astype(int) <= 2024)]
        # Convertir los valores a numeros decimales
        df["Valor"] = df["Valor"].astype(float)
        #Reiniciar los indices
        df.reset_index(inplace=True, drop=True)
        print("\nDatos de crecimiento del consumo")
        print (df.dtypes)
        print(df.head())
        print(df.tail())
        print("Cantidad de registros:", len(df))
        # Guardar los datos en un archivo CSV
        df.to_csv("Crecimiento_Consumo_Bm.csv", index=False, encoding="utf-8-sig")
    else:
        print("Error al consultar el crecimiento del consumo:", response.status_code)

# Funcion para consultar el consumo como porcentaje del PIB
def consultar_consumo_pib():
    endpoint="https://api.worldbank.org/v2/country/MEX/indicator/NE.CON.PRVT.ZS?date=2000:2024&format=json&per_page=100"
    response =requests.get(endpoint, timeout=30)
    if response.status_code == 200:
        data =response.json()
        datos= []
        # Recorrer las observaciones obtenidas
        for observacion in data[1]:
            datos.append({
                "Indicador":observacion["indicator"]["id"],
                "Periodo":observacion["date"],
                "Valor": observacion["value"]
            })
        df=pd.DataFrame(datos)
        #Filtrar los registros del periodo 2000 a 2024
        df=df[(df["Periodo"].astype(int) >= 2000) &(df["Periodo"].astype(int) <= 2024)]
        # Convertir los valores a numeros decimales
        df["Valor"] = df["Valor"].astype(float)
        # Reiniciar los indices
        df.reset_index(inplace=True, drop=True)
        print("\nDatos de consumo como porcentaje del PIB")
        print(df.dtypes)
        print(df.head())
        print(df.tail())
        print("Cantidad de registros:", len(df))
        # Guardar los datos en un archivo CSV
        df.to_csv("Consumo_Pib_Bm.csv", index=False, encoding="utf-8-sig")
    else:
        print("Error al consultar el consumo como porcentaje del PIB:", response.status_code)
#Funcion para revisar los archivos CSV extraidos
def revisar_archivos():
    print("\nRevision de archivos CSV")
    #Revisar el archivo del INPC
    print("\nArchivo: Inpc_Inegi.csv")
    df =pd.read_csv("Inpc_Inegi.csv")
    print (df.dtypes)
    print(df.head())
    print(df.tail())
    print("Valores nulos:")
    print(df.isnull().sum())
    print("Cantidad de registros:",len(df))
    #Revisar el archivo de nacimientos
    print("\nArchivo: Nacimientos_Inegi.csv")
    df= pd.read_csv("Nacimientos_Inegi.csv")
    print(df.dtypes)
    print(df.head())
    print(df.tail())
    print("Valores nulos:")
    print(df.isnull().sum())
    print("Cantidad de registros:", len(df))
    #Revisar el archivo de fecundidad
    print("\nArchivo: Fecundidad_Bm.csv")
    df = pd.read_csv("Fecundidad_Bm.csv")
    print(df.dtypes)
    print(df.head())
    print(df.tail())
    print("Valores nulos:")
    print(df.isnull().sum())
    print("Cantidad de registros:", len(df))
    #Revisar el archivo de consumo
    print("\nArchivo: Consumo_Bm.csv")
    df = pd.read_csv("Consumo_Bm.csv")
    print(df.dtypes)
    print(df.head())
    print(df.tail())
    print("Valores nulos:")
    print(df.isnull().sum())
    print("Cantidad de registros:", len(df))
    #Revisar el archivo de crecimiento del consumo
    print("\nArchivo: Crecimiento_Consumo_Bm.csv")
    df =pd.read_csv("Crecimiento_Consumo_Bm.csv")
    print(df.dtypes)
    print(df.head())
    print(df.tail())
    print("Valores nulos:")
    print(df.isnull().sum())
    print("Cantidad de registros:", len(df))
    #Revisa el archivo de consumo como porcentaje del PIB
    print("\nArchivo: Consumo_Pib_Bm.csv")
    df =pd.read_csv("Consumo_Pib_Bm.csv")
    print(df.dtypes)
    print(df.head())
    print(df.tail())
    print ("Valores nulos:")
    print(df.isnull().sum())
    print("Cantidad de registros:",len(df))

# Ejecutar las consultas y revisar los archivos
if __name__ == "__main__":
    consultar_inpc()
    consultar_nacimientos()
    consultar_fecundidad()
    consultar_consumo()
    consultar_crecimiento_consumo()
    consultar_consumo_pib()
    revisar_archivos ()
