import streamlit as st
from app.utils.functions import RenameColumns
from app.components.filtering import apply_filters 


def show_CP(self):
    st.title("Probabilidad Condicional")
    st.markdown("Hallar las probabilidades de que los eventos de la variable seleccionada ocurran, dado que los eventos de las variables condicionadoras ya han ocurrido.")

    target = st.selectbox(label="**Seleccionar Variable de interes**",options=self.vars)

    # Selección de la variable de condición
    BT = st.multiselect(label="**Selecciones las variables condicinadoras (Eventos ocurrios)**",options=[x for x in self.vars if x != target])

    with st.expander(label="**Definir condiciones**", expanded=False):
        apply_filters(self, BT, only=True)
 
    viz = self.modr.copy()
    RenameColumns(self.modr, columns=["COD_PLAN", "COD_DEPTO_RESIDENCIA", "COD_PROVINCIA", "COD_NACIONALIDAD"])

    st.dataframe(self.modr, use_container_width=True, hide_index=True)