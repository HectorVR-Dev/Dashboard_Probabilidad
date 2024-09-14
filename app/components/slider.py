import streamlit as st
from typing import Union

def CreateSlider(self, column: str, min_value: Union[int, float], max_value: Union[int, float], values: tuple, format: str, **args):
    # genera un widget interactivo de barra deslizante que permite al usuario seleccionar un rango de valores para una columna específica
    # del DataFrame. Con argumentos como el nombre de la columna, los valores mínimo y máximo, el formato de visualización y opciones
    # adicionales como el paso del slider, la función actualiza el DataFrame modr para incluir solo las filas que caen dentro del rango
    # seleccionado por el usuario en la columna especificada.
    if args:
        range = st.slider(column,
                            min_value=min_value,
                            max_value=max_value,
                            format=format,
                            value=values,
                            step=args["step"])
        if range[0] == min_value and range[1] == max_value:
            self.modr = self.modr
        else:
            self.modr = self.modr[(self.modr[column] <=
                                    range[1]) & (self.modr[column] >= range[0])]
    else:
        range = st.slider(column,
                            min_value=min_value,
                            max_value=max_value,
                            format=format,
                            value=values)
        self.modr = self.modr[(self.modr[column] <=
                                range[1]) & (self.modr[column] >= range[0])]
        