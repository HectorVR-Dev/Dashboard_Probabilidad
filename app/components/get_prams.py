import streamlit as st
from scipy.stats import norm, poisson, bernoulli, binom, expon


def get(dist_name, col = st):
    params = []  # Lista vacía para almacenar los parámetros
    
    # Distribuciones
    if dist_name == 'Normal':
        col.write("**Distribución Normal**")
        mu = col.number_input("Media (mu)", value=0.0)  # Mu es la media
        sigma = col.number_input("Desviación Estándar (sigma)", value=1.0)  # Sigma es la desviación estándar
        params.append(mu)
        params.append(sigma)
        return params

    elif dist_name == 'Poisson':
        col.write("**Distribución Poisson**")
        mu = col.number_input("Tasa promedio (mu)", value=1.0)  # Mu es la tasa promedio
        params.append(mu)

        return params

    elif dist_name == 'Bernoulli':
        col.write("**Distribución Bernoulli**")
        p = col.number_input("Probabilidad de éxito (p)", min_value=0.0, max_value=1.0, value=0.5)  # Probabilidad de éxito
        params.append(p)
        
        return params

    elif dist_name == 'Binomial':
        col.write("**Distribución Binomial**")
        n = col.number_input("Número de ensayos (n)", value=10, min_value=1)  # Número de ensayos
        p = col.number_input("Probabilidad de éxito (p)", min_value=0.0, max_value=1.0, value=0.5)  # Probabilidad de éxito
        params.append(n)
        params.append(p)
        
        return params

    elif dist_name == 'Exponencial':
        col.write("**Distribución Exponencial**")
        scale = col.number_input("Escala (1/tasa)", value=1.0)  # Escala, inverso de la tasa
        params.append(scale)

        return params
    
    return None
