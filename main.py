import numpy as np
from datasets import load_dataset

# Cargar el dataset
dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

# Extraer la lista de edades
ages = data["age"]

# Convertir la lista de edades en un arreglo de NumPy
ages_np = np.array(ages)

# Calcular el promedio de edad
average_age = np.mean(ages_np)

# Imprimir el resultado
print("El promedio de edad de las personas participantes en el estudio es:", average_age)
