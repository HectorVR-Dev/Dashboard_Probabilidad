import streamlit as st

def show_feedback(self):
        # muestra una sección titulada "Feedback y Contacto", donde se enumeran los integrantes del equipo responsable del proyecto.
        # Para cada integrante, se presenta su nombre, rol, responsabilidades, afiliación universitaria y dirección de correo electrónico.
        st.title("Feedback y Contacto")
        st.header("Integrantes")

        st.subheader("Hector Daniel Vasquez Rivera")
        st.write("**Rol**: Programador, Tester, Analista y Lider")
        st.write("**Responsabilidades**:  Diseñar la interfaz de usuario en el dashboard, para garantizar una experiencia de usuario intuitiva y atractiva. Encargado de realizar análisis de datos y generar visualizaciones significativas.")
        st.write("**Afiliación**: Estudiante en Ingeniería Mecatrónica y Estadística de la Universidad Nacional de Colombia sede de La Paz")
        st.write(
            "**Contacto** :email:: [hevasquezr@unal.edu.co](mailto:hevasquezr@unal.edu.co)")

        st.subheader("Wilhelm David Buitrago Garcia")
        st.write("**Rol**: Programador, Analista, Colider")
        st.write("**Responsabilidades**:  Desarrollar la lógica del sistema de filtros y graficas, gestionar la integración de datos, realizar análisis de datos y generar visualizaciones significativas.")
        st.write("**Afiliación**: Estudiante en Ingeniería Mecatrónica de la Universidad Nacional de Colombia sede de La Paz")
        st.write(
            "**Contacto**	:email:: [wibuitragog@unal.edu.co](mailto:wibuitragog@unal.edu.co)")

        st.subheader("Sergio Andrés Guzmán Carrascal")
        st.write("**Rol**: Programador y Documentador")
        st.write("**Responsabilidades**:  Contribuir a la lógica general de programación del proyecto. Además, de encargarse de crear documentos sobre el proyecto.")
        st.write("**Afiliación**: Estudiante en Ingeniería Mecatrónica de la Universidad Nacional de Colombia sede de La Paz")
        st.write(
            "**Contacto** :email:: [seguzmanc@unal.edu.co](mailto:seguzmanc@unal.edu.co)")