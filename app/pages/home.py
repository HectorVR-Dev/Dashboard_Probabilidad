# app/pages/home.py

import streamlit as st
import app.utils.functions as utils


def show_home(self):

    # muestra la página de inicio del dashboard. En esta página, se presenta una descripción general del propósito del
    # dashboard y se proporciona información sobre la base de datos de los estudiantes de la Universidad Nacional de
    # Colombia sede de la Paz. Se incluye una breve descripción de las características del dataset, como el número de
    # estudiantes, el número de variables y la distribución de variables numéricas y categóricas. Además, se ofrece un
    # selector de variables para que el usuario pueda explorar la descripción de cada variable seleccionada.

    st.title("Bienvenido al Dashboard de Análisis de Datos")
    st.markdown(f"""
    Este dashboard interactivo proporciona un espacio en la web para el análisis exploratorio de la base de datos de los estudiantes de la Universidad Nacional de Colombia, sede de la Paz. Aquí puedes realizar visualizaciones interactivas, aplicar filtros a los datos, obtener conclusiones clave y acceder a recursos adicionales.

    ### Descripción de la base de datos (Dinara - Listado de estudiantes activos 2024-1)
    El dataset depurado cuenta con las siguientes características:

    - Tiene **{len(self.df)}** estudiantes con **{self.nvarn+self.nvarc}** variables.
    - **{self.nvarn}** variables numéricas.
    - **{self.nvarc}** variables categóricas.

        A continuación, puede seleccionar cualquier variable para ver su respectiva descripción:
    """)


    var = st.selectbox(label="**Variable:**", options=self.vars)
    
    st.markdown(utils.desc_var(var))
