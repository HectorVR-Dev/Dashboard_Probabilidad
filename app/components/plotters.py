import streamlit as st
import app.utils.functions as functions
from app.utils.plot import histogram, barras, boxplot, scatter


def Select_Graficas(self, df):
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

        var = st.selectbox(label="**Variables permitidas:**", options=[""]+self.var_numeric)
        
        col_plot, col_desc = st.columns([2,2])
        if len(var) > 1:
            with col_plot:
                st.pyplot(histogram(df, var).get_figure(),use_container_width=True)
            with col_desc:
                with st.expander("**Descripción de variables**", expanded=True):
                    st.write(functions.desc_var(var))
        else:
            pass
    
    elif "BARRAS" in tpg:
        # Permite al usuario seleccionar una variable categórica y genera un gráfico de barras correspondiente.
        # También proporciona una descripción de la variable seleccionada.

        var = st.selectbox(label="**Variables permitidas:**", options=self.var_categoric)
        col_plot, col_desc = st.columns([2,2])
        if len(var) > 1:
            with col_plot:
                st.pyplot(barras(df, var).get_figure(), use_container_width=True)
            with col_desc:
                with st.expander("Descripción de variables", expanded=True):
                    st.write(functions.desc_var(var))
        else:
            pass

    elif "BOXPLOT" in tpg:
        # Permite al usuario seleccionar una variable categórica y una variable numérica, y genera un diagrama de caja correspondiente.
        # También proporciona una descripción de ambas variables seleccionadas.
        col1, col2 = st.columns(2)
        
        varn = col1.selectbox(label="**Variable numerica:**", options=[""]+self.var_numeric)
        varc = col2.selectbox(label="**Variable categórica:**", options=self.var_categoric)
        

        col_plot, col_desc = st.columns([2,2])
        if varc and varn:
            with col_plot:
                st.pyplot(boxplot(df, varc, varn), use_container_width=True)
            with col_desc:
                with st.expander("Descripción de variables", expanded=True):
                    st.write(functions.desc_var(varc))
                    st.write(functions.desc_var(varn))

    elif "PUNTOS" in tpg:
        # Permite al usuario seleccionar dos variables numéricas y genera un gráfico de dispersión correspondiente.
        # También proporciona una descripción de ambas variables seleccionadas.
        col1, col2 = st.columns(2)

        var1 = col1.selectbox(label="**Primera Variable:**", options=[""]+self.var_numeric)
        var2 = col2.selectbox(label="**Segunda Variable:**", options=[""]+self.var_numeric)

        col_plot, col_desc = st.columns([2,2])
        if var1 and var2:
            with col_plot:
                st.pyplot(scatter(df, var1, var2).get_figure(), use_container_width=True)

            with col_desc:
                with st.expander("Descripción de variables", expanded=True):
                    st.write(functions.desc_var(var1))
                    st.write(functions.desc_var(var2))
                    
def mostrar_mapeo_latex(valores_discretos, col=st):
    """
    Función para mostrar el mapeo discreto de una variable aleatoria en LaTeX.
    
    Args:
    - col_name: El nombre de la columna (variable aleatoria).
    - valores_discretos: Diccionario donde las claves son los valores reales 
                         y los valores son los asignados de forma discreta.
    """
    
    # LaTeX para la función de variable aleatoria
    latex_expr = f"X(a \\in \\sigma) = \\begin{{cases}}"
    
    # Generar la expresión en partes para cada valor real y su mapeo discreto
    for valor_real, valor_discreto in valores_discretos.items():
        latex_expr += f"{valor_discreto}, & \\text{{si }} a = \ {valor_real} \\\\"
    
    # Cerrar la estructura en LaTeX
    latex_expr += "\\end{cases}"
    
    # Mostrar la expresión en Streamlit
    col.latex(latex_expr)