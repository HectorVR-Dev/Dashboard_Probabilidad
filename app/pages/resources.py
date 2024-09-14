import streamlit as st

def show_resources(self):
        # muestra una sección titulada "Recursos Adicionales", donde se invita a explorar recursos relacionados
        # con el análisis de datos y las tecnologías utilizadas en el proyecto.


        lst = ['Descripción de variables',
               'Filtros interactivos', 'Graficas de variables']
        s = ''
        for i in lst:
            s += "- " + i + "\n"

        st.title("Notas de versión")
        st.info("Version 1.0 \n {}".format(s))

        st.info("Version 1.1 \n - Graficas para filtros interactivos")

        st.title("Recursos")


        st.info(
            '[GitHub](https://github.com/HectorVR-Dev/InteractiveDashboardForEDA.git)', icon="⭐")
        st.info('[StreamLit](https://streamlit.io/)', icon="ℹ️")