import streamlit as st
import app.utils.functions as functions
from app.components.plotters import Select_Graficas


def show_eda(self):
    # muestra la sección de Análisis Exploratorio de Datos (EDA, por sus siglas en inglés). En esta sección,
    # se ofrece al usuario la posibilidad de explorar y analizar los datos de manera interactiva. Se presenta
    # una breve introducción al EDA y se proporciona un selector de acciones que incluye opciones para realizar
    # estadísticas descriptivas y graficar variables. Dependiendo de la acción seleccionada por el usuario, se
    # llama a las funciones correspondientes para realizar la estadística descriptiva o la visualización de variables.
    st.title("Análisis Exploratorio de Datos (EDA)")
    st.markdown("""    
        En esta sección, puedes explorar y analizar los datos de manera interactiva.
        """)

    action = st.selectbox(label="## **Que deseas hacer:**",
                            options=["",
                                    "Estadística Descriptiva",
                                    "Visualización de Variables"])

    if action == "Estadística Descriptiva": est_desc(self)
    elif action == "Visualización de Variables": Select_Graficas(self, self.df)


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

    est_cat, index = functions.count(var,self.df)
    if index == False:
        st.dataframe(est_cat, use_container_width=True)
    else:
        st.dataframe(est_cat, hide_index=True,
                        use_container_width=True)