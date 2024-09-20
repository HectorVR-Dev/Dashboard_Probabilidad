import streamlit as st
from app.utils.functions import RenameColumns, lista_a_string, calcular_probabilidad, calcular_probabilidad_intervalo
from app.components.filtering import apply_filters
from app.components.slider import slider_intervalos


def show_CP(self):
    self.select = []
    st.title("Probabilidad Condicional")
    st.markdown("Hallar las probabilidades de que los eventos de la variable seleccionada ocurran, dado que los eventos de las variables condicionadoras ya han ocurrido.")

    target = st.selectbox(label="**Seleccionar Variable de interes**",options=self.vars)

    if target in self.var_numeric:
        with st.expander(label="La variable seleccionada es numerica, por lo tanto debe definir un rango de valores para calcular la probabilidad condicional.", expanded=False):
            min, max = slider_intervalos(self,target)
        

    # Selección de la variable de condición
    BT = st.multiselect(label="**Selecciones las variables condicinadoras (Eventos ocurrios)**",options=[x for x in self.vars if x != target])

    with st.expander(label="**Definir condiciones**", expanded=False):
        apply_filters(self, BT, only=True)
    
    RenameColumns(self.modr, columns=["COD_PLAN", "COD_DEPTO_RESIDENCIA", "COD_PROVINCIA", "COD_NACIONALIDAD"])
    
    if target in self.var_numeric:
        st.markdown(f""" **Probabilidad Condicional**: \n
                P({target} ∈ ({min},{max})|{lista_a_string(self.select)})
                """)
    else:
        st.markdown(f""" **Probabilidad Condicional**: \n
                P({target}|{lista_a_string(self.select)})
                """)

    
    if target:
        if target in self.var_numeric:
            p = calcular_probabilidad_intervalo(self.modr, target, min, max)
            st.markdown(f"La probabilidad de que la variable {target} tome valores entre {min} y {max} dadas las condiciones es:")
            st.title(f"{p:.3f}")
        else:
            st.dataframe(calcular_probabilidad(self.modr, target), use_container_width=True, hide_index=True)
