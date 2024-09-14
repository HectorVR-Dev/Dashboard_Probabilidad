import streamlit as st
from PIL import Image
import pandas as pd


import app.utils.functions as utils
from app.components.sidebar import show_sidebar

icon = Image.open('app/assets/grafico-de-dispersion.png')
st.set_page_config(page_title="Interactive Dashboard",
                    page_icon=icon, layout="wide")


class dashboard():
    def __init__(self):
        self.df = pd.read_csv("app/data/Estudiantes_clear.csv")
        self.nvarc, self.nvarn = utils.describe()
        self.var_numeric = ['AVANCE_CARRERA', 'EDAD', 'NUMERO_MATRICULAS', 'PAPA', 'PROME_ACADE', 'PBM_CALCULADO', 'PUNTAJE_ADMISION']
        self.var_categoric = ['', 'COD_PLAN', 'COD_ACCESO', 'COD_SUBACCESO', 'CONVOCATORIA', 'APERTURA', 'T_DOCUMENTO', 'GENERO', 'ESTRATO', 'COD_DEPTO_RESIDENCIA', 'MUNICIPIO_RESIDENCIA', 'COD_PROVINCIA',
                                    'MUNICIPIO_NACIMIENTO', 'COD_NACIONALIDAD', 'VICTIMAS_DEL_CONFLICTO', 'DISCAPACIDAD', 'CARACTER_COLEGIO']
        self.vars = self.df.columns.to_list()
        self.vars.insert(0, "")
        show_sidebar(self)

if __name__ == "__main__":
    dashboard()
