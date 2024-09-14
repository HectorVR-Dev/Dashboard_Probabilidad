import streamlit as st
import pandas as pd

from app.utils.functions import RenameColumns
from app.components.slider import CreateSlider
from app.components.plotters import Select_Graficas
from app.components.MultiSelect import CreateMultiSelect
from app.components.MultiSelect import _CreateMultiSelect_WithDDF, _CreateMultiSelect_WithoutDDF, _CreateMultiSelectModified, _CreateMultiselectWithNAN

def show_filters(self):
    # se encarga de mostrar filtros interactivos para personalizar el análisis de datos en la sección correspondiente de la aplicación.
    # Utiliza los elementos seleccionados por el usuario para filtrar el DataFrame principal y luego muestra los resultados en una tabla.
    # Se implementan varios tipos de filtros como selección múltiple, deslizadores para rangos numéricos y casillas de verificación.
    # La función también realiza ciertas transformaciones en los datos, como renombrar columnas y ajustar la visualización de ciertas
    # variables. Finalmente, muestra el DataFrame filtrado en una tabla con algunas columnas especiales configuradas para una mejor
    # visualización.
    self.modr = self.df

    st.title("Filtros Interactivos")
    st.write("Utiliza los filtros interactivos para personalizar tu análisis de datos.")

    BT = st.multiselect(label="**Filtros**",options=self.vars)

    with st.expander(label="**Filtros aplicados**", expanded=False):

        if "COD_PLAN" in BT:
            PLAN = pd.read_csv("app/data/COD_PLAN.csv")
            CreateMultiSelect(self,label="COD_PLAN",
                                    column="COD_PLAN",
                                    options=PLAN.iloc[:, 1].tolist(),
                                    fuction=_CreateMultiSelect_WithDDF,
                                    df=PLAN)

        if "AVANCE_CARRERA" in BT:
            CreateSlider(self,column="AVANCE_CARRERA",
                                min_value=0.,
                                max_value=100.,
                                values=(0., 100.),
                                format="%.1f")

        if "COD_ACCESO" in BT:
            ACCESO = pd.read_csv("app/data/COD_ACCESO.csv")
            CreateMultiSelect(self,label="COD_ACCESO",
                                    column="COD_ACCESO",
                                    options=ACCESO.iloc[:, 1].tolist(),
                                    fuction=_CreateMultiSelect_WithDDF,
                                    df=ACCESO)

        if "COD_SUBACCESO" in BT:
            SUBACCESO = pd.read_csv("app/data/COD_SUBACCESO.csv")
            CreateMultiSelect(self,label="COD_SUBACCESO",
                                    column="COD_SUBACCESO",
                                    options=SUBACCESO.iloc[:, 1].tolist(),
                                    fuction=_CreateMultiSelect_WithDDF,
                                    df=SUBACCESO)

        if "GENERO" in BT:
            CreateMultiSelect(self,label="GENERO",
                                    column="GENERO",
                                    options=self.modr["GENERO"].drop_duplicates(),
                                    fuction=_CreateMultiSelect_WithoutDDF)

        if "EDAD" in BT:
            min = self.df["EDAD"].min()
            max = self.df["EDAD"].max()
            CreateSlider(self,column="EDAD",
                                min_value=min,
                                max_value=max,
                                values=(min, max),
                                format="%d")

        if "PAPA" in BT:
            min = self.df["PAPA"].min()
            max = self.df["PAPA"].max()
            CreateSlider(self,column="PAPA",
                                min_value=min,
                                max_value=max,
                                values=(min, max),
                                format="%.1f")

        if "PROME_ACADE" in BT:
            min = self.df["PROME_ACADE"].min()
            max = self.df["PROME_ACADE"].max()
            CreateSlider(self,column="PROME_ACADE",
                                min_value=min,
                                max_value=max,
                                values=(min, max),
                                format="%0.1f")

        if "PBM_CALCULADO" in BT:
            min = self.df["PBM_CALCULADO"].min()
            max = self.df["PBM_CALCULADO"].max()
            CreateSlider(self,column="PBM_CALCULADO",
                                min_value=min,
                                max_value=max,
                                values=(min, max),
                                format="%d")

        if "CONVOCATORIA" in BT:
            CreateMultiSelect(self,label="CONVOCATORIA",
                                    column="CONVOCATORIA",
                                    options=self.df["CONVOCATORIA"].drop_duplicates(),
                                    fuction=_CreateMultiSelect_WithoutDDF)

        if "APERTURA" in BT:
            CreateMultiSelect(self,label="APERTURA",
                                    column="APERTURA",
                                    options=self.df["APERTURA"].drop_duplicates(),
                                    fuction=_CreateMultiSelect_WithoutDDF)

        if "T_DOCUMENTO" in BT:
            CreateMultiSelect(self,label="T_DOCUMENTO",
                                    column="T_DOCUMENTO",
                                    options=self.df["T_DOCUMENTO"].drop_duplicates(),
                                    fuction=_CreateMultiSelect_WithoutDDF)

        if "NUMERO_MATRICULAS" in BT:
            min = int(self.df["NUMERO_MATRICULAS"].min())
            max = int(self.df["NUMERO_MATRICULAS"].max())
            CreateSlider(self,column="NUMERO_MATRICULAS",
                                min_value=min,
                                max_value=max,
                                values=(min, max),
                                format="%d",
                                step=1)

        if "ESTRATO" in BT:
            min = int(self.df["ESTRATO"].min())
            max = int(self.df["ESTRATO"].max())
            CreateSlider(self,column="ESTRATO",
                                min_value=min,
                                max_value=max,
                                values=(min, max),
                                format="%d",
                                step=1)

        if "VICTIMAS_DEL_CONFLICTO" in BT:
            CreateMultiSelect(self,label="VICTIMAS_DEL_CONFLICTO",
                                    column="VICTIMAS_DEL_CONFLICTO",
                                    options=["SI", "NO"],
                                    fuction=_CreateMultiSelectModified)

        if "DISCAPACIDAD" in BT:
            CreateMultiSelect(self,label="DISCAPACIDAD",
                                    column="DISCAPACIDAD",
                                    options=self.df["DISCAPACIDAD"].drop_duplicates(),
                                    fuction=_CreateMultiSelect_WithoutDDF)

        if "CARACTER_COLEGIO" in BT:
            CreateMultiSelect(self,label="CARACTER_COLEGIO",
                                    column="CARACTER_COLEGIO",
                                    options=self.df["CARACTER_COLEGIO"].drop_duplicates(),
                                    fuction=_CreateMultiSelect_WithoutDDF)

        if "PUNTAJE_ADMISION" in BT:
            min = self.df["PUNTAJE_ADMISION"].min()
            max = self.df["PUNTAJE_ADMISION"].max()
            CreateSlider(self,column="PUNTAJE_ADMISION",
                                min_value=min,
                                max_value=max,
                                values=(min, max),
                                format="%0.1f")

        if "COD_DEPTO_RESIDENCIA" in BT:
            CDRESIDENCIA = pd.read_csv(
                "app/data/COD_DEPTO_RESIDENCIA.csv")
            CreateMultiSelect(self,label="COD_DEPTO_RESIDENCIA",
                                    column="COD_DEPTO_RESIDENCIA",
                                    options=CDRESIDENCIA.iloc[:, 1],
                                    fuction=_CreateMultiSelect_WithDDF,
                                    df=CDRESIDENCIA)

        if "MUNICIPIO_RESIDENCIA" in BT:
            CreateMultiSelect(self,label="MUNICIPIO_RESIDENCIA",
                                    column="MUNICIPIO_RESIDENCIA",
                                    options=self.df["MUNICIPIO_RESIDENCIA"].dropna().drop_duplicates(),
                                    fuction=_CreateMultiselectWithNAN)

        if "COD_PROVINCIA" in BT:
            CPROVINCIA = pd.read_csv("app/data/COD_PROVINCIA.csv")
            CreateMultiSelect(self,label="COD_PROVINCIA",
                                    column="COD_PROVINCIA",
                                    options=CPROVINCIA.iloc[:, 1],
                                    fuction=_CreateMultiSelect_WithDDF,
                                    df=CPROVINCIA)
            
        if "MUNICIPIO_NACIMIENTO" in BT:
            CreateMultiSelect(self,label="MUNICIPIO_NACIMIENTO",
                                    column="MUNICIPIO_NACIMIENTO",
                                    options=self.df["MUNICIPIO_NACIMIENTO"].dropna().drop_duplicates(), 
                                    fuction=_CreateMultiselectWithNAN)

        if "COD_NACIONALIDAD" in BT:
            CNACIONALIDAD = pd.read_csv("app/data/COD_NACIONALIDAD.csv")
            CreateMultiSelect(self,label="COD_NACIONALIDAD",
                                    column="COD_NACIONALIDAD",
                                    options=CNACIONALIDAD.iloc[:, 1],
                                    fuction=_CreateMultiSelect_WithDDF,
                                    df=CNACIONALIDAD)


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
