import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def histogram(df, data: str):
    # La función histogram() recibe un nombre de columna de datos y genera un histograma correspondiente utilizando la biblioteca Seaborn.
    # Se crea un DataFrame con la columna de datos seleccionada y se utiliza seaborn para trazar el histograma. Se establecen etiquetas
    # adecuadas para los ejes x e y del histograma. Finalmente, se devuelve el objeto del histograma.
    dataframe = pd.DataFrame(df[data])
    histogram_params = {'AVANCE_CARRERA': [-0.05, 100.05, 5, 0, 100, 10],
                        'EDAD': [9.5, 60.05, 1, 10, 60, 5],
                        'NUMERO_MATRICULAS': [-0.5, 15.5, 1, 0, 15, 1],
                        'PAPA': [-0.05, 5.05, 0.1, 0, 5.1, 0.5],
                        'PROME_ACADE': [-0.05, 5.05, 0.1, 0, 5.1, 0.5],
                        'PBM_CALCULADO': [-0.05, 100.05, 1, 0, 100, 10],
                        'PUNTAJE_ADMISION': [199.5, 1000.5, 25, 200, 1100, 100]
                        }
    [stard, end, step, x_stard, x_end, x_step] = histogram_params[data]

    bins_edges = np.arange(stard, end, step)
    plot = sns.histplot(x=data, data=dataframe, color="#A31D31", bins=bins_edges)
    
    plt.xticks(np.arange(x_stard, x_end, x_step))
    plot.set_xlabel(data)
    plot.set_ylabel("Recuento")
    plt.gcf().set_facecolor("#F3F0F0")
    return plot

def barras(df, data: str):

    # toma el nombre de una variable categórica y produce un gráfico de barras correspondiente utilizando Seaborn.
    # Calcula la frecuencia de cada categoría en la variable seleccionada y ordena las etiquetas si la variable es
    # del tipo 'COD'. Luego, crea el gráfico de barras con Seaborn, estableciendo las etiquetas en el eje x y los
    # valores en el eje y. Ajusta el formato de las etiquetas del eje x según ciertas variables categóricas específicas
    # y añade etiquetas a las barras si corresponde. Finalmente, establece las etiquetas adecuadas para los ejes x e y y
    # devuelve el objeto del gráfico de barras generado.

    count = df[data].value_counts()

    if (data == "APERTURA") or (data == "CONVOCATORIA"):
        count = count.sort_index(ascending=True)
    
    label = count.index.tolist()
    values = count.values.tolist()

    if data[:3] == 'COD':
        if data != "COD_PLAN":
            label = [str(int(lab)) for lab in label]

    plot = sns.barplot(x=label, y=values, color="#A31D31")

    if data == "MUNICIPIO_NACIMIENTO":
        rotation = 90
        fontsize = 4
        plot.set_xticklabels(plot.get_xticklabels(), rotation=rotation, fontsize=fontsize)

    elif (data == "MUNICIPIO_RESIDENCIA") or (data == "CONVOCATORIA") or (data == "APERTURA") or (data == "DISCAPACIDAD"):
        rotation = 45
        plot.bar_label(plot.containers[0], fontsize=8)
        plot.set_xticklabels(plot.get_xticklabels(),rotation=rotation, horizontalalignment='right')

    else:
        plot.bar_label(plot.containers[0], fontsize=10)

    plot.set_xlabel(data)
    plot.set_ylabel("Recuento")
    plt.gcf().set_facecolor("#F3F0F0")
    return plot

def boxplot(df, varc: str, varn: str):

    # La función boxplot() recibe los nombres de una variable categórica y una variable numérica, y genera un diagrama de caja correspondiente
    # utilizando Seaborn. Se extraen los valores de ambas variables del DataFrame principal y se crea el diagrama de caja con Seaborn, especificando
    # la variable categórica en el eje x y la variable numérica en el eje y. Se establecen etiquetas adecuadas para los ejes x e y del diagrama,
    # y se aplican ajustes adicionales al formato de las etiquetas del eje x en función de ciertas variables categóricas específicas. Finalmente,
    # se devuelve el objeto del diagrama de caja.

    label = df[[varc]].iloc[:, 0].tolist()
    values = df[[varn]].iloc[:, 0].tolist()
    plot = sns.boxplot(x=label, y=values, data=df, color="#A31D31")

    plot.set_xlabel(varc)
    plot.set_ylabel(varn)

    if varc == "MUNICIPIO_NACIMIENTO":
        plot.set_xticklabels(plot.get_xticklabels(), rotation=90, fontsize=4)

    elif (varc == "MUNICIPIO_RESIDENCIA") or (varc == "CONVOCATORIA") or (varc == "APERTURA") or (varc == "DISCAPACIDAD"):
        plot.set_xticklabels(plot.get_xticklabels(), rotation=45, horizontalalignment='right')

    plot = plt.gcf()
    plt.gcf().set_facecolor("#F3F0F0")
    return plot

def scatter(df, var1: str, var2: str):

    # toma los nombres de dos variables numéricas y genera un gráfico de dispersión correspondiente utilizando Seaborn.
    # Extrae los valores de ambas variables del DataFrame principal, y luego crea el gráfico de dispersión con Seaborn,
    # especificando la primera variable en el eje x y la segunda variable en el eje y. Además, utiliza el valor de la
    # segunda variable para codificar el color de los puntos en el gráfico. Se establecen etiquetas adecuadas para los
    # ejes x e y, y finalmente se devuelve el objeto del gráfico de dispersión generado.


    values1 = df[[var1]].iloc[:, 0].tolist()
    values2 = df[[var2]].iloc[:, 0].tolist()
    plot = sns.scatterplot(x=values1, y=values2, data=df, hue=values2)

    plot.set_xlabel(var1)
    plot.set_ylabel(var2)
    plt.gcf().set_facecolor("#F3F0F0")
    return plot