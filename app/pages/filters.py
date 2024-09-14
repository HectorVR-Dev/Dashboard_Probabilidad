import streamlit as st

def show_filters(self):
        # se encarga de mostrar filtros interactivos para personalizar el análisis de datos en la sección correspondiente de la aplicación.
        # Utiliza los elementos seleccionados por el usuario para filtrar el DataFrame principal y luego muestra los resultados en una tabla.
        # Se implementan varios tipos de filtros como selección múltiple, deslizadores para rangos numéricos y casillas de verificación.
        # La función también realiza ciertas transformaciones en los datos, como renombrar columnas y ajustar la visualización de ciertas
        # variables. Finalmente, muestra el DataFrame filtrado en una tabla con algunas columnas especiales configuradas para una mejor
        # visualización.

        st.title("Filtros Interactivos")

        st.write("Utiliza los filtros interactivos para personalizar tu análisis de datos.")