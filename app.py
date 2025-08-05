import polars as pl
import time

inicio = time.time()

# Leer el archivo CSV
df = pl.read_csv("Licitaciones.csv")

# Mostrar primeras filas
print("📄 Primeras filas del DataFrame:")
print(df.head())

# Estadísticas generales
print("\n📊 Estadísticas generales:")
print(df.describe())

# Filtrar por tipo: Salud
print("\n🩺 Licitaciones de tipo Salud:")
salud = df.filter(pl.col("tipo") == "Salud")
print(salud)

#filtrar por tipo de entidad
print("\n🏛️ Licitaciones de tipo de entidad:")
entidad = df.filter(pl.col("entidad")=="Ministerio de Agricultura")



# Filtrar por entidad: Gobierno Regional
print("\n🏛️ Licitaciones de 'Gobierno Regional':")
entidad = df.filter(pl.col("entidad") == "Gobierno Regional")
print(entidad)



# Ordenar por monto descendente
print("\n💰 Licitaciones ordenadas por monto:")
ordenado = df.sort("monto", descending=True)
print(ordenado.head(10))  # Solo muestra las 10 más altas

fin = time.time()
print(f"\n⏱️ Tiempo de ejecución: {fin - inicio:.4f} segundos")
