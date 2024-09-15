import streamlit as st

from app.utils.functions import RenameColumns
from app.components.plotters import Select_Graficas
from app.components.filtering import apply_filters 

def show_filters(self):
    # se encarga de mostrar filtros interactivos para personalizar el análisis de datos en la sección correspondiente de la aplicación.
    # Utiliza los elementos seleccionados por el usuario para filtrar el DataFrame principal y luego muestra los resultados en una tabla.
    # Se implementan varios tipos de filtros como selección múltiple, deslizadores para rangos numéricos y casillas de verificación.
    # La función también realiza ciertas transformaciones en los datos, como renombrar columnas y ajustar la visualización de ciertas
    # variables. Finalmente, muestra el DataFrame filtrado en una tabla con algunas columnas especiales configuradas para una mejor
    # visualización.

    st.title("Filtros Interactivos")
    st.write("Utiliza los filtros interactivos para personalizar tu análisis de datos.")

    BT = st.multiselect(label="**Filtros**",options=self.vars)

    with st.expander(label="**Filtros aplicados**", expanded=False):
        apply_filters(self, BT)

    if BT:
        st.write(f"El **{round(len(self.modr)/len(self.df)*100, 2)}%** de los datos corresponden a los filtros seleccionados, es decir, se han encontrado **{len(self.modr)}**  elementos de **{len(self.df)}** datos.")
    
    viz = self.modr.copy()
    RenameColumns(self.modr, columns=["COD_PLAN", "COD_DEPTO_RESIDENCIA", "COD_PROVINCIA", "COD_NACIONALIDAD"])

    st.dataframe(self.modr,column_config={"AVANCE_CARRERA": st.column_config.ProgressColumn("AVANCE_CARRERA",
                                                                                    help="El avance del estudiante en su carrera actual",
                                                                                    min_value=0.0,
                                                                                    max_value=100.0,
                                                                                    format="%f"),
                                "PUNTAJE_ADMISION": st.column_config.ProgressColumn("PUNTAJE_ADMISION",
                                                                                    help="Puntaje obtenido por el estudiante en la prueba de admision",
                                                                                    min_value=None,
                                                                                    max_value=888.484,
                                                                                    format="%f")},
                    use_container_width=True,
                    hide_index=True)
    
    if BT and len(self.modr) != 0:
        st.write("**Visualización de variables**")
        Select_Graficas(self,viz)
