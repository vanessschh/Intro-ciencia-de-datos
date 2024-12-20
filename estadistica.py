# -*- coding: utf-8 -*-
"""estadistica.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10wLQOdzhvzoVO8mCPVfRzxzMkjZaqdbT
"""

#promedio
def promedio(datos):
  """
  Calcula el promedio (media) de una lista de datos, eliminando los valores NaN.

  Parámetros:
  datos : Lista de números (que pueden incluir valores NaN).

  Retorna:
  float: El promedio de los valores no NaN de la lista.
  """
  datos_sinNan=[]
  for x in datos:
    if x == x:
      datos_sinNan.append(x)
  return sum(datos_sinNan)/len(datos_sinNan)

#mediana
def mediana(datos):
  """
    Calcula la mediana de una lista de datos, eliminando los valores NaN.

    Parámetros:
    datos : Lista de números (que pueden incluir valores NaN).

    Retorna:
    float: El valor de la mediana de los datos, después de eliminar los NaN.
    """
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
  """
    Calcula la moda de una lista de datos, eliminando los valores NaN.

    Parámetros:
    datos : Lista de números (que pueden incluir valores NaN).

    Retorna:
    list: Una lista de los valores que aparecen con mayor frecuencia en los datos.
    """
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
  """
    Calcula el rango (diferencia entre el valor máximo y mínimo) de una lista de datos, eliminando los valores NaN.

    Parámetros:
    datos : Lista de números (que pueden incluir valores NaN).

    Retorna:
    float: El rango de los datos no NaN.
    """
  datos_sinNan=[]
  for x in datos:
    if x == x:
      datos_sinNan.append(x)
  return max(datos_sinNan)-min(datos_sinNan)

#varianza
def varianza(datos):
  """
    Calcula la varianza de una lista de datos, eliminando los valores NaN.

    Parámetros:
    datos : Lista de números (que pueden incluir valores NaN).

    Retorna:
    float: La varianza de los datos no NaN.
    """
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
  """
    Calcula la desviación estándar de una lista de datos, eliminando los valores NaN.

    Parámetros:
    datos : Lista de números (que pueden incluir valores NaN).

    Retorna:
    float: La desviación estándar de los datos no NaN.
    """
  datos_sinNan=[]
  for x in datos:
    if x == x:
      datos_sinNan.append(x)
  return varianza(datos_sinNan) ** 0.5

#cuartiles
def cuartiles(datos):
  """
    Calcula los cuartiles (Q1, Q2, Q3) de una lista de datos, eliminando los valores NaN.

    Parámetros:
    datos : Lista de números (que pueden incluir valores NaN).

    Retorna:
    tuple: Los tres cuartiles Q1, Q2 (mediana) y Q3 de los datos.
    """
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
  """
    Calcula el rango intercuartílico (Q3 - Q1) de una lista de datos, eliminando los valores NaN.

    Parámetros:
    datos : Lista de números (que pueden incluir valores NaN).

    Retorna:
    float: El rango intercuartílico de los datos no NaN.
    """
  datos_sinNan=[]
  for x in datos:
    if x == x:
      datos_sinNan.append(x)
    Q1, Q2, Q3 = cuartiles(datos_sinNan)
  return Q3 - Q1

#desviación mediana absoluta
def desv_mediana_abs(datos):
  """
    Calcula la desviación mediana absoluta de una lista de datos, eliminando los valores NaN.

    Parámetros:
    datos : Lista de números (que pueden incluir valores NaN).

    Retorna:
    float: La desviación mediana absoluta de los datos no NaN.
    """
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
  """
    Calcula el percentil k de una lista de datos, eliminando los valores NaN.

    Parámetros:
    datos : Lista de números (que pueden incluir valores NaN).
    k : El percentil a calcular (un valor entre 0 y 100).

    Retorna:
    float: El valor correspondiente al percentil k de los datos no NaN.
    """
  datos_sinNan = []
  for x in datos:
      if x == x:
          datos_sinNan.append(x)
  datos_ordenados = sorted(datos_sinNan)
  n = len(datos_ordenados)
  posicion = (k / 100) * (n - 1)
  if posicion.is_integer():
      return datos_ordenados[int(posicion) - 1]
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

    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_x_squared = sum(xi ** 2 for xi in x)
    sum_y_squared = sum(yi ** 2 for yi in y)

    numerator = n * sum_xy - sum_x * sum_y
    denominator = ((n * sum_x_squared - sum_x ** 2) * (n * sum_y_squared - sum_y ** 2)) ** 0.5

    if denominator == 0:
        return 0
    return numerator / denominator
