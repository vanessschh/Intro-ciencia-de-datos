# -*- coding: utf-8 -*-
"""estadistica.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10wLQOdzhvzoVO8mCPVfRzxzMkjZaqdbT
"""

#promedio
def promedio(datos):
  datos_sinNan=[]
  for x in datos:
    if x == x:
      datos_sinNan.append(x)
  return sum(datos_sinNan)/len(datos_sinNan)

#mediana
def mediana(datos):
  datos_sinNan=[]
  for x in datos:
    if x == x:
      datos_sinNan.append(x)
  datos_ordenados=sorted(datos_sinNan)
  n = len(datos_ordenados)
  if n % 2 == 0:
    return (datos_ordenados[n//2-1] + datos_ordenados[n//2])/2
  else:
    return datos_ordenados[n//2]

#moda
def moda(datos):
  datos_sinNan=[]
  for x in datos:
    if x == x:
      datos_sinNan.append(x)

  frecuencias = {}
  for x in datos_sinNan:
    if x in frecuencias:
      frecuencias[x] += 1
    else:
      frecuencias[x] = 1
  maxima_frec = max(frecuencias.values())
  modas = []
  for k, v in frecuencias.items():
    if v == maxima_frec:
      modas.append(k)
  return modas



#rango
def rango(datos):
  datos_sinNan=[]
  for x in datos:
    if x == x:
      datos_sinNan.append(x)
  return max(datos_sinNan)-min(datos_sinNan)

#varianza
def varianza(datos):
  datos_sinNan=[]
  for x in datos:
    if x == x:
      datos_sinNan.append(x)

  suma_cuadrados = 0
  for x in datos_sinNan:
    suma_cuadrados += (x - promedio(datos_sinNan)) ** 2
  return suma_cuadrados / len(datos_sinNan)

#desviación estándar
def desviacion_estandar(datos):
  datos_sinNan=[]
  for x in datos:
    if x == x:
      datos_sinNan.append(x)
  return varianza(datos_sinNan) ** 0.5

#cuartiles
def cuartiles(datos):
  datos_sinNan=[]
  for x in datos:
    if x == x:
      datos_sinNan.append(x)

  datos_ordenados = sorted(datos_sinNan)
  n = len(datos_ordenados)
  pos_Q1 = (n - 1) * 0.25
  indice_inferior_Q1 = int(pos_Q1)
  indice_superior_Q1 = indice_inferior_Q1 + 1
  if indice_superior_Q1 < n:
    Q1 = datos_ordenados[indice_inferior_Q1] + (pos_Q1 - indice_inferior_Q1) * (datos_ordenados[indice_superior_Q1] - datos_ordenados[indice_inferior_Q1])
  else:
    Q1 = datos_ordenados[indice_inferior_Q1]

  Q2 = mediana(datos_ordenados)

  pos_Q3 = (n - 1) * 0.75
  indice_inferior_Q3 = int(pos_Q3)
  indice_superior_Q3 = indice_inferior_Q3 + 1
  if indice_superior_Q3 < n:
    Q3 = datos_ordenados[indice_inferior_Q3] + (pos_Q3 - indice_inferior_Q3) * (datos_ordenados[indice_superior_Q3] - datos_ordenados[indice_inferior_Q3])
  else:
    Q3 = datos_ordenados[indice_inferior_Q3]
  return Q1, Q2, Q3


#rango intercualtílico
def rango_intercuartilico(datos):
  datos_sinNan=[]
  for x in datos:
    if x == x:
      datos_sinNan.append(x)
    Q1, Q2, Q3 = cuartiles(datos_sinNan)
  return Q3 - Q1

#desviación mediana absoluta
def desv_mediana_abs(datos):
  datos_sinNan=[]
  for x in datos:
    if x == x:
      datos_sinNan.append(x)

  diferencias_abs = []
  for x in datos_sinNan:
      diferencias_abs.append(abs(x - mediana(datos_sinNan)))
  return mediana(diferencias_abs)

#percentiles
def percentil(datos, k):
    # Eliminar valores NaN
    datos_sinNan = []
    for x in datos:
        if x == x:
            datos_sinNan.append(x)
    # Ordenar los datos
    datos_ordenados = sorted(datos_sinNan)
    # Calcular la posición del percentil
    n = len(datos_ordenados)
    posicion = (k / 100) * (n - 1)
    # Si la posición es un número entero, devolvemos el valor en esa posición
    if posicion.is_integer():
        return datos_ordenados[int(posicion) - 1]
    # Si la posición no es un número entero, interpolamos entre los dos valores más cercanos
    else:
        lower = datos_ordenados[int(posicion) - 1]
        upper = datos_ordenados[int(posicion)]
        return lower + (upper - lower) * (posicion - int(posicion))


def calcular_coeficiente_correlacion(x, y):
    """
    Calcula el coeficiente de correlación de Pearson entre dos listas de datos

    Parámetros:
    x : Datos de la primera variable.
    y : Datos de la segunda variable.

    Retorna:
    float:coeficiente de correlación de Pearson.
    """
    n = len(x)

    # Calcular las sumas necesarias
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_x_squared = sum(xi ** 2 for xi in x)
    sum_y_squared = sum(yi ** 2 for yi in y)

    # Aplicar la fórmula del coeficiente de correlación de Pearson
    numerator = n * sum_xy - sum_x * sum_y
    denominator = ((n * sum_x_squared - sum_x ** 2) * (n * sum_y_squared - sum_y ** 2)) ** 0.5

    if denominator == 0:
        return 0
    return numerator / denominator