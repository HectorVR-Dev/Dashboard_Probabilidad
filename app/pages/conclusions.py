import streamlit as st

def show_conclusions(self):
        # presenta los hallazgos del análisis de datos en forma de una lista numerada con descripciones breves de cada hallazgo.
        st.title("Hallazgos del Análisis de Datos")
        st.write("""
        1. **Distribución de Género:**
           - El 55% de los estudiantes son hombres y el 45% son mujeres. Esta diferencia es más evidente en el programa de Mecatrónica, donde solo el 8.3% son mujeres.

        2. **Situación Socioeconómica:**
           - El 72% de los estudiantes tienen el Puntaje de Matrícula Básica (PBM) entre 0 y 10, lo que indica que no pagan matrícula y una gran parte se puede considerar vulnerable. Además, casi el 90% de los estudiantes son de estratos 1 y 2.

        3. **Rendimiento Académico:**
           - A medida que se avanza en la carrera, el promedio académico tiende a estabilizarse en alrededor de 4.2.

        4. **Preferencia de Carreras:**
           - Las ingenierías son los programas más demandados, con los puntajes de admisión más altos y la menor tasa de deserción, indicando una mayor cantidad de estudiantes activos.

        5. **Residencia Estudiantil:**
           - La mayoría de los estudiantes residen en el municipio de Valledupar.

        6. **Correlación entre Tipo de Colegio y Puntaje de Admisión:**
           - Se aprecia una posible correlación entre el tipo de colegio y el puntaje de admisión, con estudiantes de colegios privados tendiendo a tener puntajes más altos que los de colegios públicos y nocturnos. Esto sugiere diferencias en la calidad de la educación entre diferentes tipos de colegios.
        
        7. **Origen Regional:**
           - Más del 90% de los estudiantes son nacidos en la región Caribe, donde se encuentra ubicada la universidad.
        """)