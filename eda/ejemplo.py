import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('cars.csv')

# Mostrar las primeras filas del DataFrame
print("Primeras filas del DataFrame:")
print(df.head())

# Resumen estadístico de las columnas numéricas
print("\nResumen estadístico:")
print(df.describe())

# Comprobar si hay valores nulos
print("\nValores nulos en cada columna:")
print(df.isnull().sum())

# Distribución del precio de los automóviles
plt.figure(figsize=(8, 6))
plt.hist(df['Price'], bins=20, color='blue', edgecolor='black')
plt.title('Distribución de Precios de Automóviles')
plt.xlabel('Precio')
plt.ylabel('Frecuencia')
plt.show()

# Scatter plot entre Precio y Kilometraje
plt.figure(figsize=(8, 6))
plt.scatter(df['Mileage'], df['Price'], color='red')
plt.title('Precio vs. Kilometraje')
plt.xlabel('Kilometraje')
plt.ylabel('Precio')
plt.show()

# Promedio de precio por marca
mean_price_by_make = df.groupby('Make')['Price'].mean()
print("\nPromedio de precio por marca:")
print(mean_price_by_make)

