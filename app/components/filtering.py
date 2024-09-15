import pandas as pd
from app.components.slider import CreateSlider
from app.components.MultiSelect import CreateMultiSelect
from app.components.MultiSelect import _CreateMultiSelect_WithDDF, _CreateMultiSelect_WithoutDDF, _CreateMultiSelectModified, _CreateMultiselectWithNAN

def apply_filters(self, BT, only=False):
    self.modr = self.df
    if "COD_PLAN" in BT:
        PLAN = pd.read_csv("app/data/COD_PLAN.csv")
        CreateMultiSelect(self,only,label="COD_PLAN",
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
        CreateMultiSelect(self,only,label="COD_ACCESO",
                                column="COD_ACCESO",
                                options=ACCESO.iloc[:, 1].tolist(),
                                fuction=_CreateMultiSelect_WithDDF,
                                df=ACCESO)

    if "COD_SUBACCESO" in BT:
        SUBACCESO = pd.read_csv("app/data/COD_SUBACCESO.csv")
        CreateMultiSelect(self,only,label="COD_SUBACCESO",
                                column="COD_SUBACCESO",
                                options=SUBACCESO.iloc[:, 1].tolist(),
                                fuction=_CreateMultiSelect_WithDDF,
                                df=SUBACCESO)

    if "GENERO" in BT:
        CreateMultiSelect(self,only,label="GENERO",
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
        CreateMultiSelect(self,only,label="CONVOCATORIA",
                                column="CONVOCATORIA",
                                options=self.df["CONVOCATORIA"].drop_duplicates(),
                                fuction=_CreateMultiSelect_WithoutDDF)

    if "APERTURA" in BT:
        CreateMultiSelect(self,only,label="APERTURA",
                                column="APERTURA",
                                options=self.df["APERTURA"].drop_duplicates(),
                                fuction=_CreateMultiSelect_WithoutDDF)

    if "T_DOCUMENTO" in BT:
        CreateMultiSelect(self,only,label="T_DOCUMENTO",
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
        CreateMultiSelect(self,only,label="VICTIMAS_DEL_CONFLICTO",
                                column="VICTIMAS_DEL_CONFLICTO",
                                options=["SI", "NO"],
                                fuction=_CreateMultiSelectModified)

    if "DISCAPACIDAD" in BT:
        CreateMultiSelect(self,only,label="DISCAPACIDAD",
                                column="DISCAPACIDAD",
                                options=self.df["DISCAPACIDAD"].drop_duplicates(),
                                fuction=_CreateMultiSelect_WithoutDDF)

    if "CARACTER_COLEGIO" in BT:
        CreateMultiSelect(self,only,label="CARACTER_COLEGIO",
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
        CreateMultiSelect(self,only,label="COD_DEPTO_RESIDENCIA",
                                column="COD_DEPTO_RESIDENCIA",
                                options=CDRESIDENCIA.iloc[:, 1],
                                fuction=_CreateMultiSelect_WithDDF,
                                df=CDRESIDENCIA)

    if "MUNICIPIO_RESIDENCIA" in BT:
        CreateMultiSelect(self,only,label="MUNICIPIO_RESIDENCIA",
                                column="MUNICIPIO_RESIDENCIA",
                                options=self.df["MUNICIPIO_RESIDENCIA"].dropna().drop_duplicates(),
                                fuction=_CreateMultiselectWithNAN)

    if "COD_PROVINCIA" in BT:
        CPROVINCIA = pd.read_csv("app/data/COD_PROVINCIA.csv")
        CreateMultiSelect(self,only,label="COD_PROVINCIA",
                                column="COD_PROVINCIA",
                                options=CPROVINCIA.iloc[:, 1],
                                fuction=_CreateMultiSelect_WithDDF,
                                df=CPROVINCIA)
        
    if "MUNICIPIO_NACIMIENTO" in BT:
        CreateMultiSelect(self,only,label="MUNICIPIO_NACIMIENTO",
                                column="MUNICIPIO_NACIMIENTO",
                                options=self.df["MUNICIPIO_NACIMIENTO"].dropna().drop_duplicates(), 
                                fuction=_CreateMultiselectWithNAN)

    if "COD_NACIONALIDAD" in BT:
        CNACIONALIDAD = pd.read_csv("app/data/COD_NACIONALIDAD.csv")
        CreateMultiSelect(self,only,label="COD_NACIONALIDAD",
                                column="COD_NACIONALIDAD",
                                options=CNACIONALIDAD.iloc[:, 1],
                                fuction=_CreateMultiSelect_WithDDF,
                                df=CNACIONALIDAD)
