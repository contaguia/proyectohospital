import pandas as pd
import matplotlib.pyplot as plt

# Crear un DataFrame
df = pd.read_csv("hospital.csv")
# df = pd.read_csv("discapacitado.csv",encoding="unicode_escape")
#print(df)  
#f.to_csv("atencionhospital.csv")

# print(df.head(10))      # Primeras 5 filas
# print(df.tail())       # Últimas 5 filas
# print(df.info())      # Información general
# print(df.describe())   # Estadísticas descriptivas

# Selección de columna
# print(df["EDAD"])

# Selección de varias columnas
# print(df[["CICLO DE VIDA", "REGIMEN"]])

# Filtrado de datos
# print(df[df["ANO DE LA CONSULTA"] > 2022])
           
# print(df[["INGRESO", "TRIMESTRE"]] )


# print(df[["MUNICIPIO","INGRESO","EDAD",]])
# print(df["EDAD"].mean())
# print(df["EDAD"].median())
# print(df["EDAD"].std())

# Contar consultas por género
gender_count = data['GENERO'].value_counts()

# Gráfico
gender_count.plot(kind='bar', color=['skyblue', 'pink'])
plt.title('Distribución de Consultas por Género')
plt.xlabel('Género')
plt.ylabel('Cantidad de Consultas')
plt.show()