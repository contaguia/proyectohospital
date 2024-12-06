import pandas as pd

# Crear un DataFrame
df = pd.read_csv("poblacion.csv")
#print(df)  
df.to_csv("archivo.csv")

# print(df.head(10))      # Primeras 5 filas
# print(df.tail())       # Últimas 5 filas
# print(df.info())      # Información general
# print(df.describe())   # Estadísticas descriptivas

# # Selección de columna
# print(df["COL"])

# # Selección de varias columnas
# df[["Nombre", "Edad"]]

# # Filtrado de datos
# df[df["Edad"] > 30]
           
# print(df[["Date", "COL"]] )


# print(df[["Date","COL","CHN"]])
# print(df["COL"].mean())
# print(df["COL"].median())
# print(df["COL"].std())

