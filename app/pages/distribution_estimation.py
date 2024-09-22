import streamlit as st
import app.utils.functions as utils
from app.utils.plot import histogram, barras
from app.components.plotters import mostrar_mapeo_latex
from app.utils.plot import plot_barras_dist, plot_histograma_dist
from app.components.get_prams import get, get_latex_formula
from scipy.stats import (norm, poisson, bernoulli, binom, expon, geom, nbinom, uniform, 
                         beta, gamma, chi2, t, lognorm, pareto, randint)


distributions = {
    None: None,

    # Distribuciones continuas (pdf)
    'Normal': norm.pdf,
    'Exponencial': expon.pdf,
    'Uniforme': uniform.pdf,
    'Beta': beta.pdf,
    'Gamma': gamma.pdf,
    'Chi-cuadrado': chi2.pdf,
    't de Student': t.pdf,
    'Log-Normal': lognorm.pdf,
    'Pareto': pareto.pdf,

    # Distribuciones discretas (pmf)
    'Poisson': poisson.pmf,
    'Bernoulli': bernoulli.pmf,
    'Binomial': binom.pmf,
    'Geométrica': geom.pmf,
    'Binomial Negativa': nbinom.pmf,
    'Uniforme Discreta': randint.pmf
}
['Normal','Exponencial','Uniforme','Beta','Gamma','Chi-cuadrado','t de Student','Log-Normal','Pareto']

def show_DE(self):
    st.title("Estimación de Distribución de Probabilidad")
    st.markdown("Hallar la distribución de probabilidad de la variable seleccionada.")
    target = st.selectbox(label="**Seleccionar Variable de interes**", options=self.vars)

    

    if target:
        with st.expander(label="**Descripcion Variable**", expanded=False):
            st.markdown(utils.desc_var(target))
        col1, col2 = st.columns([2,3])
        col2.subheader("Panel de Control")
        col21, col22 = col2.columns([1,1])
        
        
        if target in self.var_numeric:
            if col21.checkbox("Estandarizar"):

                params = None
                distribution = col2.selectbox("Elige una distribución",[None,'Normal',
                                                                        'Exponencial',
                                                                        'Uniforme','Beta',
                                                                        'Gamma',
                                                                        'Chi-cuadrado',
                                                                        't de Student',
                                                                        'Log-Normal',
                                                                        'Pareto'] ,index=0)
                if distribution:
                    params = get(distribution, col2)
                col1.pyplot(plot_histograma_dist(self.df, target, distributions[distribution], params).get_figure(), use_container_width=True)


            else:
                col1.pyplot(histogram(self.df, target).get_figure(), use_container_width=True)

        else:       
            if col21.checkbox("Crear variable aleatoria"):
                va, mapeo = utils.conv_va_discreta(self.df, target)

                with col2.expander(label="**Ver Variable aletaoria**", expanded=False):
                    mostrar_mapeo_latex(mapeo)

                if col22.checkbox("Estandarizar"):
                    params = None
                    estandar = utils.estandarizar_columna_categorica(va)
                    distribution = col2.selectbox("Elige una distribución",[None,'Poisson',
                                                                            'Bernoulli',
                                                                            'Binomial',
                                                                            'Geométrica',
                                                                            'Binomial Negativa',
                                                                            'Uniforme Discreta'],index=0)
                    if distribution:
                        params = get(distribution, col2)
                    col1.pyplot(plot_barras_dist(estandar, distributions[distribution], params).get_figure(), use_container_width=True)


                else:
                    col1.pyplot(barras(va, 'Valores').get_figure(), use_container_width=True)
            else:
                col22.checkbox("Estandarizar", value=False, disabled=True)
                col1.pyplot(barras(self.df, target).get_figure(), use_container_width=True)

