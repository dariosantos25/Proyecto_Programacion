import pandas as pd

# Transformar los datos mensuales del INPC a datos anuales
def transformar_inpc():
    df = pd.read_csv("Inpc_Inegi.csv")
    # Convertir el periodo a formato fecha
    df["Periodo"] = pd.to_datetime(df["Periodo"], format="%Y/%m")

    # Obtener el año del periodo
    df["Periodo"] = df["Periodo"].dt.year

    # Calcular el promedio anual de cada indicador
    df = df.groupby(["Indicador", "Periodo"])["Valor"].mean().reset_index()

    # Ordenar los datos por indicador y año
    df.sort_values(["Indicador", "Periodo"], inplace=True)

    # Reiniciar los indices
    df.reset_index(inplace=True, drop=True)

    print("\nDatos del INPC transformados")
    print(df.dtypes)
    print(df.head())
    print(df.tail())
    print("Cantidad de registros:", len(df))

    # Guardar los datos transformados
    df.to_csv("Inpc_Anual.csv", index=False, encoding="utf-8-sig")

# Ordenar los datos de nacimientos por año
def transformar_nacimientos():
    df = pd.read_csv("Nacimientos_Inegi.csv")

    # Ordenar los datos por año
    df.sort_values("Periodo", inplace=True)

    # Reiniciar los indices
    df.reset_index(inplace=True, drop=True)
    print("\nDatos de nacimientos transformados")
    print(df.dtypes)
    print(df.head())
    print(df.tail())
    print("Cantidad de registros:", len(df))

    # Guardar los datos transformados
    df.to_csv("Nacimientos_Transformados.csv", index=False, encoding="utf-8-sig")


# Ordenar los datos de fecundidad por año
def transformar_fecundidad():
    df = pd.read_csv("Fecundidad_Bm.csv")

    # Ordenar los datos por año
    df.sort_values("Periodo", inplace=True)

    # Reiniciar los indices
    df.reset_index(inplace=True, drop=True)
    print("\nDatos de fecundidad transformados")
    print(df.dtypes)
    print(df.head())
    print(df.tail())
    print("Cantidad de registros:", len(df))

    # Guardar los datos transformados
    df.to_csv("Fecundidad_Transformada.csv", index=False, encoding="utf-8-sig")


# Ordenar los datos de consumo por año
def transformar_consumo():
    df = pd.read_csv("Consumo_Bm.csv")

    # Ordenar los datos por año
    df.sort_values("Periodo", inplace=True)

    # Reiniciar los indices
    df.reset_index(inplace=True, drop=True)
    print("\nDatos de consumo transformados")
    print(df.dtypes)
    print(df.head())
    print(df.tail())
    print("Cantidad de registros:", len(df))

    # Guardar los datos transformados
    df.to_csv("Consumo_Transformado.csv", index=False, encoding="utf-8-sig")


# Ordenar los datos de crecimiento del consumo por año
def transformar_crecimiento():
    df = pd.read_csv("Crecimiento_Consumo_Bm.csv")

    # Ordenar los datos por año
    df.sort_values("Periodo", inplace=True)

    # Reiniciar los indices
    df.reset_index(inplace=True, drop=True)
    print("\nDatos de crecimiento del consumo transformados")
    print(df.dtypes)
    print(df.head())
    print(df.tail())
    print("Cantidad de registros:", len(df))

    # Guardar los datos transformados
    df.to_csv("Crecimiento_Consumo_Transformado.csv", index=False, encoding="utf-8-sig")


# Ordenar los datos de consumo como porcentaje del PIB por año
def transformar_consumo_pib():
    df = pd.read_csv("Consumo_Pib_Bm.csv")

    # Ordenar los datos por año
    df.sort_values("Periodo", inplace=True)

    # Reiniciar los indices
    df.reset_index(inplace=True, drop=True)
    print("\nDatos de consumo como porcentaje del PIB transformados")
    print(df.dtypes)
    print(df.head())
    print(df.tail())
    print("Cantidad de registros:", len(df))

    # Guardar los datos transformados
    df.to_csv("Consumo_Pib_Transformado.csv", index=False, encoding="utf-8-sig")


# Preparar los datos del INPC para su integración
def preparar_inpc():
    df = pd.read_csv("Inpc_Anual.csv")

    # Convertir los indicadores en columnas
    df = df.pivot(index="Periodo", columns="Indicador", values="Valor")

    # Quitar el nombre del indice de las columnas
    df.columns.name =None

    # Reiniciar los indices
    df.reset_index(inplace=True)

    # Cambiar los nombres de los indicadores
    df.rename(columns={
        910394: "INPC_General",
        910395: "INPC_Mercancias",
        910397: "INPC_Servicios",
        910398: "INPC_Agropecuarios",
        910392:
            "INPC_Energeticos_Gobierno"
    }, inplace=True)

    # Ordenar los datos por año
    df.sort_values("Periodo", inplace=True)

    # Reiniciar los indices
    df.reset_index(inplace=True, drop=True)
    print("\nDatos del INPC preparados")
    print(df.dtypes)
    print(df.head())
    print(df.tail())
    print("Cantidad de registros:", len(df))

    # Guardar los datos preparados
    df.to_csv("Inpc_Preparado.csv", index=False, encoding="utf-8-sig")


# Revisar los archivos generados durante la transformación
def revisar_archivos():
    df_inpc = pd.read_csv("Inpc_Anual.csv")
    df_nacimientos = pd.read_csv("Nacimientos_Transformados.csv")
    df_fecundidad = pd.read_csv("Fecundidad_Transformada.csv")
    df_consumo = pd.read_csv("Consumo_Transformado.csv")
    df_crecimiento = pd.read_csv("Crecimiento_Consumo_Transformado.csv")
    df_consumo_pib = pd.read_csv("Consumo_Pib_Transformado.csv")
    df_inpc_preparado = pd.read_csv("Inpc_Preparado.csv")

    print("\nRevisión de archivos transformados")

    print("\nINPC anual")
    print("Registros:", len(df_inpc))
    print("Valores nulos:")
    print(df_inpc.isnull().sum())
    print(df_inpc.dtypes)

    print("\nNacimientos")
    print("Registros:", len(df_nacimientos))
    print("Valores nulos:")
    print(df_nacimientos.isnull().sum())
    print(df_nacimientos.dtypes)

    print("\nFecundidad")
    print("Registros:", len(df_fecundidad))
    print("Valores nulos:")
    print(df_fecundidad.isnull().sum())
    print(df_fecundidad.dtypes)

    print("\nConsumo")
    print("Registros:", len(df_consumo))
    print("Valores nulos:")
    print(df_consumo.isnull().sum())
    print(df_consumo.dtypes)

    print("\nCrecimiento del consumo")
    print("Registros:", len(df_crecimiento))
    print("Valores nulos:")
    print(df_crecimiento.isnull().sum())
    print(df_crecimiento.dtypes)

    print("\nConsumo como porcentaje del PIB")
    print("Registros:", len(df_consumo_pib))
    print("Valores nulos:")
    print(df_consumo_pib.isnull().sum())
    print(df_consumo_pib.dtypes)

    print("\nINPC preparado")
    print("Registros:", len(df_inpc_preparado))
    print("Valores nulos:")
    print(df_inpc_preparado.isnull().sum())
    print(df_inpc_preparado.dtypes)


# Ejecutar las transformaciones en el orden correspondiente
if __name__ == "__main__":
    transformar_inpc()
    transformar_nacimientos()
    transformar_fecundidad()
    transformar_consumo()
    transformar_crecimiento()
    transformar_consumo_pib()

    # Preparar el INPC después de calcular sus promedios anuales
    preparar_inpc()

    # Revisar los archivos transformados
    revisar_archivos()