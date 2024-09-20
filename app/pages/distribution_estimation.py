import streamlit as st
import app.utils.functions as utils
from app.utils.plot import histogram, barras
from app.components.plotters import mostrar_mapeo_latex


def show_DE(self):
    st.title("Estimación de Distribución de Probabilidad")
    st.markdown("Hallar la distribución de probabilidad de la variable seleccionada.")
    target = st.selectbox(label="**Seleccionar Variable de interes**", options=self.vars)
    col1, col2 = st.columns([2,3,])

    col21, col22 = col2.columns([1,1])

    if target in self.var_numeric:
        pass
        #utils.plot_distribution(self.modr, target)
    elif target:
        if col22.checkbox("Estandarizar"):
            pass
        if col21.checkbox("Crear variable aleatoria"):
            va, mapeo = utils.conv_va_discreta(self.df, target)
            with col2.expander(label="**Ver Variable aletaoria**", expanded=False):
                mostrar_mapeo_latex(mapeo)
        
        col1.latex(f"Funcion de distribucion \tilde{{f}}:")
        col1.pyplot(barras(self.df, target).get_figure(),use_container_width=True)
