import streamlit as st
import pandas as pd

def CreateMultiSelect(self,only:bool, label: str, column: str, options: list, fuction, **args):
    # crea un widget de selección múltiple que permite al usuario seleccionar opciones de una lista proporcionada.
    if args:
        fuction(self,only,label, column, options, **args)
    else:
        fuction(self,only,label, column, options)


def _CreateMultiSelect_WithDDF(self, only: bool,
                                label: str,
                                column: str,
                                options: list,
                                df: pd.DataFrame):
    # crea un widget de selección múltiple que muestra las opciones proporcionadas en forma de lista desplegable.
    # Cuando el usuario selecciona una o más opciones, la función actualiza el DataFrame modr para incluir solo las
    # filas donde los valores de la columna especificada (column) coinciden con las opciones seleccionadas por el usuario.
    # Utiliza un DataFrame auxiliar (df) para mapear las selecciones del usuario a los valores correspondientes de la
    # columna especificada.
    if only:
        Select = [st.selectbox(label=label, options=options)]
        self.select.append([column, Select[0]])
        Select = df[df.iloc[:, 1].isin(Select)].iloc[:, 0].tolist()
    else:
        Select = st.multiselect(label=label, options=options)
        Select = df[df.iloc[:, 1].isin(Select)].iloc[:, 0].tolist()

    self.modr = self.modr[self.modr[column].isin(Select)]


def _CreateMultiSelect_WithoutDDF(self, only: bool,
                                    label: str,
                                    column: str,
                                    options: list):
    # crea un widget de selección múltiple sin utilizar un DataFrame adicional. Muestra las opciones proporcionadas
    # en una lista desplegable y permite al usuario seleccionar una o más opciones. Luego, la función actualiza el
    # DataFrame modr para incluir solo las filas donde los valores de la columna especificada (column) coinciden con
    # las opciones seleccionadas por el usuario.
    if only:
        Select = [st.selectbox(label=label, options=options)]
        self.select.append([column, Select[0]])
    else:
        Select = st.multiselect(label=label, options=options)

    self.modr = self.modr[self.modr[column].isin(Select)]

def _CreateMultiSelectModified(self, only: bool,
                                label: str,
                                column: str,
                                options: list):
    # crea un widget de selección múltiple modificado para manejar una variable binaria específica. Permite al usuario seleccionar entre
    # las opciones proporcionadas, y si se selecciona "SI" pero no "NO", filtra el DataFrame modr para incluir solo las filas donde la
    # columna especificada (column) tenga el valor "SI". Del mismo modo, si se selecciona "NO" pero no "SI", filtra el DataFrame para
    # incluir solo las filas donde la columna tenga el valor "NO". Si ambas opciones están seleccionadas o ninguna está seleccionada,
    # no se realiza ningún filtrado y se mantiene el DataFrame original.
    if only:
        Select = [st.selectbox(label=label, options=options)]
        self.select.append([column, Select[0]])
    else:
        Select = st.multiselect(label=label, options=options)

    if "SI" in Select and "NO" not in Select:
        self.modr = self.modr[self.modr[column].isin(["SI"])]

    elif "NO" in Select and "SI" not in Select:
        self.modr = self.modr[self.modr[column].isin(["NO"])]

    else:
        self.modr = self.modr

        
    

def _CreateMultiselectWithNAN(self, only: bool,
                                label: str,
                                column: str,
                                options: list):
    # crea un widget de selección múltiple que permite al usuario seleccionar opciones de una lista proporcionada.
    # Si no se selecciona ninguna opción, el DataFrame modr no se filtra y permanece sin cambios. Si se seleccionan
    # opciones, el DataFrame se filtra para incluir solo las filas donde la columna especificada (column) tenga valores
    # que coincidan con las opciones seleccionadas.
    if only:
        Select = [st.selectbox(label=label, options=options)]
        self.select.append([column, Select[0]])
    else:
        Select = st.multiselect(label=label,options=options)

    if Select:
        self.modr = self.modr[self.modr[column].isin(Select)]
    