import streamlit as st
import app.utils.functions as utils
from app.utils.plot import histogram, barras
from app.components.plotters import mostrar_mapeo_latex
from app.utils.plot import plot_barras_dist
from app.components.get_prams import get
from scipy.stats import (norm, poisson, bernoulli, binom, expon, geom, nbinom, uniform, 
                         beta, gamma, chi2, t, lognorm, pareto)


# Diccionario con distribuciones de SciPy
distributions = {
    None: None,
    'Normal': norm.pdf,  # Distribución continua (pdf)
    'Poisson': poisson.pmf,  # Distribución discreta (pmf)
    'Bernoulli': bernoulli.pmf,  # Distribución discreta (pmf)
    'Binomial': binom.pmf,  # Distribución discreta (pmf)
    'Exponencial': expon.pdf,  # Distribución continua (pdf)
    'Geométrica': geom.pmf,  # Distribución discreta (pmf)
    'Binomial Negativa': nbinom.pmf,  # Distribución discreta (pmf)
    'Uniforme': uniform.pdf,  # Distribución continua (pdf)
    'Beta': beta.pdf,  # Distribución continua (pdf)
    'Gamma': gamma.pdf,  # Distribución continua (pdf)
    'Chi-cuadrado': chi2.pdf,  # Distribución continua (pdf)
    't de Student': t.pdf,  # Distribución continua (pdf)
    'Log-Normal': lognorm.pdf,  # Distribución continua (pdf)
    'Pareto': pareto.pdf  # Distribución continua (pdf)
}

def show_DE(self):
    st.title("Estimación de Distribución de Probabilidad")
    st.markdown("Hallar la distribución de probabilidad de la variable seleccionada.")
    target = st.selectbox(label="**Seleccionar Variable de interes**", options=self.vars)

    with st.expander(label="**Descripcion Variable**", expanded=False):
        st.markdown(utils.desc_var(target))
    col1, col2 = st.columns([2,3])

    if target:
        col2.subheader("Panel de Control")
        col21, col22 = col2.columns([1,1])
        activate = col21.checkbox("Crear variable aleatoria")
        
        
        if target in self.var_numeric:
            if activate:
                pass
            else:
                pass
                #col22.checkbox("Estandarizar", value=False, disabled=True)
                #col1.pyplot(histogram(self.df, target).get_figure(), use_container_width=True)
            #utils.plot_distribution(self.modr, target)
        elif target:       
            if activate:

                va, mapeo = utils.conv_va_discreta(self.df, target)

                with col2.expander(label="**Ver Variable aletaoria**", expanded=False):
                    mostrar_mapeo_latex(mapeo)

                if col22.checkbox("Estandarizar"):
                    params = None
                    estandar = utils.estandarizar_columna_frecuencia(va)
                    distribution = col2.selectbox("Elige una distribución",[None,'Poisson',
                                                                            'Bernoulli',
                                                                            'Binomial',
                                                                            'Geométrica',
                                                                            'Binomial Negativa'])
                    if distribution:
                        params = get(distribution, col2)
                    col1.pyplot(plot_barras_dist(estandar, distributions[distribution], params).get_figure(), use_container_width=True)


                else:
                    col1.pyplot(barras(va, 'Valores').get_figure(), use_container_width=True)
            else:
                col22.checkbox("Estandarizar", value=False, disabled=True)
                col1.pyplot(barras(self.df, target).get_figure(), use_container_width=True)

