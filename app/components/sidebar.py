import streamlit as st
from PIL import Image


from app.pages import home, EDA, filters, conclusions, resources, feedback

def show_sidebar(self):
    img = Image.open('app/assets/UNAL.png')
    st.sidebar.title("Navegación")

    page = st.sidebar.radio(    label="empty_label", options=["Inicio", "EDA and Visualización", "Filtros Interactivos",
                                "Conclusiones", "Notas de version y recursos adicionales", "Feedback y Contacto"],
                                label_visibility='hidden')

    st.sidebar.image(img, width=200)

    pages = {   'Inicio': home.show_home,
                'EDA and Visualización': EDA.show_eda,
                'Filtros Interactivos': filters.show_filters,
                'Conclusiones': conclusions.show_conclusions,
                'Notas de version y recursos adicionales': resources.show_resources,
                'Feedback y Contacto': feedback.show_feedback}

    pages[page](self)
