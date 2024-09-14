import streamlit as st
from PIL import Image


from app.pages import home, EDA, filters, conclusions, resources, feedback

def show_sidebar(self):
    img = Image.open('app/assets/logo_UNAL_2.png')
    st.sidebar.image(img)
    st.sidebar.title("Navegación")

    page = st.sidebar.radio(    label="empty_label", options=["Inicio", "EDA and Visualización", "Filtros Interactivos",
                                "Conclusiones", "Notas de version y recursos adicionales", "Feedback y Contacto"],
                                label_visibility='hidden')

    pages = {   'Inicio': home.show_home,
                'EDA and Visualización': EDA.show_eda,
                'Filtros Interactivos': filters.show_filters,
                'Conclusiones': conclusions.show_conclusions,
                'Notas de version y recursos adicionales': resources.show_resources,
                'Feedback y Contacto': feedback.show_feedback}

    pages[page](self)
