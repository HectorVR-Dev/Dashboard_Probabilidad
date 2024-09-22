import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white")

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
    plot = sns.histplot(x=data, data=dataframe, color="#b2b2b2", bins=bins_edges)
    
    plt.xticks(np.arange(x_stard, x_end, x_step))
    plot.set_xlabel(data)
    plot.set_title('Histograma de ' + data)
    plot.set_ylabel("Recuento")
    
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

    plot = sns.barplot(x=label, y=values, color="#b2b2b2")

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
    plot.set_title('Gráfico de barras de ' + data)
    plot.set_ylabel("Recuento")
    return plot

def boxplot(df, varc: str, varn: str):

    # La función boxplot() recibe los nombres de una variable categórica y una variable numérica, y genera un diagrama de caja correspondiente
    # utilizando Seaborn. Se extraen los valores de ambas variables del DataFrame principal y se crea el diagrama de caja con Seaborn, especificando
    # la variable categórica en el eje x y la variable numérica en el eje y. Se establecen etiquetas adecuadas para los ejes x e y del diagrama,
    # y se aplican ajustes adicionales al formato de las etiquetas del eje x en función de ciertas variables categóricas específicas. Finalmente,
    # se devuelve el objeto del diagrama de caja.

    label = df[[varc]].iloc[:, 0].tolist()
    values = df[[varn]].iloc[:, 0].tolist()
    plot = sns.boxplot(x=label, y=values, data=df, color="#b2b2b2")

    plot.set_xlabel(varc)
    plot.set_ylabel(varn)
    plot.set_title('Diagrama de caja de ' + varn + ' por ' + varc)

    if varc == "MUNICIPIO_NACIMIENTO":
        plot.set_xticklabels(plot.get_xticklabels(), rotation=90, fontsize=4)

    elif (varc == "MUNICIPIO_RESIDENCIA") or (varc == "CONVOCATORIA") or (varc == "APERTURA") or (varc == "DISCAPACIDAD"):
        plot.set_xticklabels(plot.get_xticklabels(), rotation=45, horizontalalignment='right')

    plot = plt.gcf()
    
    
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
    plot.set_title('Gráfico de dispersión de ' + var1 + ' vs ' + var2)
    
    return plot


def plot_barras_dist(df, dist_func=None, dist_params=None):
    fig, ax = plt.subplots()

    # Gráfico de barras
    ax.bar(df['Valores'], df['Frecuencia'], color="#b2b2b2")

    for index, row in df.iterrows():
        ax.text(row['Valores'], row['Frecuencia'] + 0.01, round(row['Frecuencia'], 2), color='black', ha="center")

    max_frecuencia = df['Frecuencia'].max()

    if dist_func and dist_params:
        # Calcular la distribución discreta
        x = np.arange(min(df['Valores']), max(df['Valores']) + 1)
        y = dist_func(x, *dist_params)

        if max(y) < max_frecuencia:
            ax.set_ylim(0, max_frecuencia * 1.2)
        # Graficar la distribución seleccionada
        ax.plot(x, y, 'ro-', label='Función de Distribución')
    else:
        ax.set_ylim(0, max_frecuencia * 1.2)

    ax.set_xlabel('Valores X=x')
    ax.set_ylabel('Probabilidad')
    ax.set_title('Datos con Función de Distribución')
    ax.legend(loc='upper left')

    return fig


def plot_histograma_dist(df, data: str, dist_func=None, dist_params=None):
    # Define los parámetros de los histogramas para cada variable
    histogram_params = {
        'AVANCE_CARRERA': [-0.05, 100.05, 5, 0, 100, 10],
        'EDAD': [9.5, 60.05, 1, 10, 60, 5],
        'NUMERO_MATRICULAS': [-0.5, 15.5, 1, 0, 15, 1],
        'PAPA': [-0.05, 5.05, 0.1, 0, 5.1, 0.5],
        'PROME_ACADE': [-0.05, 5.05, 0.1, 0, 5.1, 0.5],
        'PBM_CALCULADO': [-0.05, 100.05, 1, 0, 100, 10],
        'PUNTAJE_ADMISION': [199.5, 1000.5, 25, 200, 1100, 100]
    }

    # Extraer parámetros para la columna seleccionada
    stard, end, step, x_stard, x_end, x_step = histogram_params[data]
    bins_edges = np.arange(stard, end, step)

    # Crear el histograma normalizado
    fig, ax = plt.subplots()
    frecuencias, bins, _ = ax.hist(df[data], bins=bins_edges, density=True, alpha=0.5, color="#b2b2b2", edgecolor="black")

    # Graficar la función de distribución continua si se proporciona
    if dist_func and dist_params:
        x = np.linspace(stard, end, 1000)
        y = dist_func(x, *dist_params)
        ax.plot(x, y, 'r-', lw=2, label='Función de Distribución')

    # Etiquetas y título
    ax.set_xlabel(data)
    ax.set_ylabel("Densidad de Probabilidad")
    ax.set_title('Histograma de ' + data)
    ax.legend(loc='upper right')

    plt.xticks(np.arange(x_stard, x_end, x_step))
    plt.show()

    return fig