import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import app.utils.functions as utils


def show_eda(self):
    # muestra la sección de Análisis Exploratorio de Datos (EDA, por sus siglas en inglés). En esta sección,
    # se ofrece al usuario la posibilidad de explorar y analizar los datos de manera interactiva. Se presenta
    # una breve introducción al EDA y se proporciona un selector de acciones que incluye opciones para realizar
    # estadísticas descriptivas y graficar variables. Dependiendo de la acción seleccionada por el usuario, se
    # llama a las funciones correspondientes para realizar la estadística descriptiva o la visualización de variables.

    st.markdown("""
        # **Análisis Exploratorio de Datos**
                
        En esta sección, puedes explorar y analizar los datos de manera interactiva.
        """)

    action = st.selectbox(label="## **Que deseas hacer:**",
                            options=["",
                                    "Estadística Descriptiva",
                                    "Visualización de Variables"])

    if action == "Estadística Descriptiva": est_desc(self)
    elif action == "Visualización de Variables": Select_Graficas(self)


def est_desc(self):
    # La función est_desc() permite al usuario realizar estadísticas descriptivas sobre las variables del conjunto de datos.
    # Dependiendo del tipo de variable seleccionada (numérica o categórica), se presentan opciones diferentes:
    # Si se selecciona una variable numérica, se muestra un selector múltiple para elegir una o más variables numéricas.
    # Luego, se calculan y muestran las estadísticas descriptivas (como media, mediana, mínimo, máximo, etc.) para las
    # variables seleccionadas.
    # Si se selecciona una variable categórica, se muestra un selector para elegir una variable categórica.
    # Posteriormente, se llama a la función desc_cat() para mostrar los datos de la variable categórica seleccionada.

    typeVar = st.selectbox(label="**Tipo de Variable:**",
                            options=["",
                                    "Numérica",
                                    "Categórica"])
    if typeVar == "Numérica":
        variable_seleccionada = st.multiselect(label="Selecciona las variables numéricas **(Una o Mas)**.",
                                                options=self.var_numeric)

        if variable_seleccionada != []:
            estadisticas = self.df[variable_seleccionada].describe()
            st.dataframe(estadisticas, use_container_width=True)

    elif typeVar == "Categórica":
        variable_seleccionada = st.selectbox(label="**Selecciona las variable categórica:**", options=self.var_categoric)

        if variable_seleccionada:
            desc_cat(self, variable_seleccionada)

def desc_cat(self, var):

    # La función desc_cat() muestra los datos de una variable categórica seleccionada.
    # Se utiliza la función count() para obtener el conteo de valores únicos de la
    # variable categórica y se muestra el DataFrame resultante. Si el índice del
    # DataFrame es "nh" (no ocultar índice), se muestra el DataFrame con el índice
    # visible; de lo contrario, se oculta el índice del DataFrame.

    est_cat, index = utils.count(var,self.df)
    if index == False:
        st.dataframe(est_cat, use_container_width=True)
    else:
        st.dataframe(est_cat, hide_index=True,
                        use_container_width=True)

def Select_Graficas(self):
    # La función Select_Graficas() permite al usuario seleccionar el tipo de gráfico que desea generar y las variables que
    # desea utilizar en la visualización. Dependiendo del tipo de gráfico seleccionado, se muestran opciones específicas
    # para seleccionar las variables y se generan los gráficos correspondientes. Aquí está un resumen de lo que hace cada
    # sección del código:
    tpg = st.selectbox(label="**Tipo de grafico:**",
                        options=["",
                                "HISTOGRAMA",
                                "BARRAS",
                                "BOXPLOT",
                                "PUNTOS"])


    if "HISTOGRAMA" in tpg:
        # Permite al usuario seleccionar una variable numérica y genera un histograma correspondiente.
        # También proporciona una descripción de la variable seleccionada.

        var = st.selectbox(label="**Variables permitidas:**",
                            options=[""]+self.var_numeric)
        if len(var) > 1:
            st.pyplot(histogram(self, var).get_figure(),use_container_width=True)

            with st.expander("**Descripción de variables**", expanded=False):
                st.write(utils.desc_var(var))
        else:
            pass
    
    elif "BARRAS" in tpg:
        # Permite al usuario seleccionar una variable categórica y genera un gráfico de barras correspondiente.
        # También proporciona una descripción de la variable seleccionada.

        var = st.selectbox(label="**Variables permitidas:**", options=self.var_categoric)

        if len(var) > 1:
            st.pyplot(barras(self, var).get_figure(), use_container_width=True)

            with st.expander("Descripción de variables", expanded=False):
                st.write(utils.desc_var(var))
        else:
            pass

    elif "BOXPLOT" in tpg:
        # Permite al usuario seleccionar una variable categórica y una variable numérica, y genera un diagrama de caja correspondiente.
        # También proporciona una descripción de ambas variables seleccionadas.
        col1, col2 = st.columns(2)

        varc = col1.selectbox(label="**Variable categórica:**", options=self.var_categoric)
        
        varn = col2.selectbox(label="**Variable numerica:**", options=[""]+self.var_numeric)

        if varc and varn:
            st.pyplot(self.boxplot(self, varc, varn), use_container_width=True)
            
        with st.expander("Descripción de variables", expanded=False):
            st.write(utils.desc_var(varc))
            st.write(utils.desc_var(varn))

    elif "PUNTOS" in tpg:
        # Permite al usuario seleccionar dos variables numéricas y genera un gráfico de dispersión correspondiente.
        # También proporciona una descripción de ambas variables seleccionadas.
        col1, col2 = st.columns(2)

        var1 = col1.selectbox(label="**Primera Variable:**", options=[""]+self.var_numeric)

        var2 = col2.selectbox(label="**Segunda Variable:**", options=[""]+self.var_numeric)

        if var1 and var2:
            st.pyplot(self.scatter(self, var1, var2).get_figure(), use_container_width=True)

            with st.expander("Descripción de variables", expanded=False):
                st.write(utils.desc_var(var1))
                st.write(utils.desc_var(var2))

def histogram(self, data: str):
    # La función histogram() recibe un nombre de columna de datos y genera un histograma correspondiente utilizando la biblioteca Seaborn.
    # Se crea un DataFrame con la columna de datos seleccionada y se utiliza seaborn para trazar el histograma. Se establecen etiquetas
    # adecuadas para los ejes x e y del histograma. Finalmente, se devuelve el objeto del histograma.
    dataframe = pd.DataFrame(self.df[data])

    plot = sns.histplot(x=data, data=dataframe, color="#A31D31")
    plot.set_xlabel(data)
    plot.set_ylabel("Recuento")
    plt.gcf().set_facecolor("#F3F0F0")
    return plot

def barras(self, data: str):

    # toma el nombre de una variable categórica y produce un gráfico de barras correspondiente utilizando Seaborn.
    # Calcula la frecuencia de cada categoría en la variable seleccionada y ordena las etiquetas si la variable es
    # del tipo 'COD'. Luego, crea el gráfico de barras con Seaborn, estableciendo las etiquetas en el eje x y los
    # valores en el eje y. Ajusta el formato de las etiquetas del eje x según ciertas variables categóricas específicas
    # y añade etiquetas a las barras si corresponde. Finalmente, establece las etiquetas adecuadas para los ejes x e y y
    # devuelve el objeto del gráfico de barras generado.

    count = self.df[data].value_counts()

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

def boxplot(self, varc: str, varn: str):

    # La función boxplot() recibe los nombres de una variable categórica y una variable numérica, y genera un diagrama de caja correspondiente
    # utilizando Seaborn. Se extraen los valores de ambas variables del DataFrame principal y se crea el diagrama de caja con Seaborn, especificando
    # la variable categórica en el eje x y la variable numérica en el eje y. Se establecen etiquetas adecuadas para los ejes x e y del diagrama,
    # y se aplican ajustes adicionales al formato de las etiquetas del eje x en función de ciertas variables categóricas específicas. Finalmente,
    # se devuelve el objeto del diagrama de caja.

    label = self.df[[varc]].iloc[:, 0].tolist()
    values = self.df[[varn]].iloc[:, 0].tolist()
    plot = sns.boxplot(x=label, y=values, data=self.df, color="#A31D31")

    plot.set_xlabel(varc)
    plot.set_ylabel(varn)

    if varc == "MUNICIPIO_NACIMIENTO":
        plot.set_xticklabels(plot.get_xticklabels(), rotation=90, fontsize=4)

    elif (varc == "MUNICIPIO_RESIDENCIA") or (varc == "CONVOCATORIA") or (varc == "APERTURA") or (varc == "DISCAPACIDAD"):
        plot.set_xticklabels(plot.get_xticklabels(), rotation=45, horizontalalignment='right')

    plot = plt.gcf()
    plt.gcf().set_facecolor("#F3F0F0")
    return plot

def scatter(self, var1: str, var2: str):

    # toma los nombres de dos variables numéricas y genera un gráfico de dispersión correspondiente utilizando Seaborn.
    # Extrae los valores de ambas variables del DataFrame principal, y luego crea el gráfico de dispersión con Seaborn,
    # especificando la primera variable en el eje x y la segunda variable en el eje y. Además, utiliza el valor de la
    # segunda variable para codificar el color de los puntos en el gráfico. Se establecen etiquetas adecuadas para los
    # ejes x e y, y finalmente se devuelve el objeto del gráfico de dispersión generado.


    values1 = self.df[[var1]].iloc[:, 0].tolist()
    values2 = self.df[[var2]].iloc[:, 0].tolist()
    plot = sns.scatterplot(x=values1, y=values2, data=self.df, hue=values2)

    plot.set_xlabel(var1)
    plot.set_ylabel(var2)
    plt.gcf().set_facecolor("#F3F0F0")
    return plot