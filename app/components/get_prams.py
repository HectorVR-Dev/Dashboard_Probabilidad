import streamlit as st
from scipy.stats import norm, poisson, bernoulli, binom, expon


def get(dist_name, col = st):
    params = []  # Lista vacía para almacenar los parámetros
    
    # Distribuciones
    if dist_name == 'Normal':
        
        col.write("**Distribución Normal**")
        get_latex_formula(dist_name, col)
        mu = col.number_input("Media (mu)", value=0.0)  # Media
        sigma = col.number_input("Desviación estándar (sigma)", value=1.0, min_value=0.0)  # Desviación estándar
        params.append(mu)
        params.append(sigma)
        
        return params

    elif dist_name == 'Poisson':
        
        col.write("**Distribución Poisson**")
        get_latex_formula(dist_name, col)
        lambda_ = col.number_input("Tasa media (lambda)", value=1.0, min_value=0.0)  # Parámetro lambda
        params.append(lambda_)
        
        return params

    elif dist_name == 'Bernoulli':
        
        col.write("**Distribución Bernoulli**")
        get_latex_formula(dist_name, col)
        p = col.number_input("Probabilidad de éxito (p)", min_value=0.0, max_value=1.0, value=0.5)  # Probabilidad de éxito
        params.append(p)
        
        return params

    elif dist_name == 'Binomial':
        
        col.write("**Distribución Binomial**")
        get_latex_formula(dist_name, col)
        n = col.number_input("Número de ensayos (n)", value=10, min_value=1)  # Número de ensayos
        p = col.number_input("Probabilidad de éxito (p)", min_value=0.0, max_value=1.0, value=0.5)  # Probabilidad de éxito
        params.append(n)
        params.append(p)
        
        return params

    elif dist_name == 'Exponencial':
        
        col.write("**Distribución Exponencial**")
        get_latex_formula(dist_name, col)
        lambda_ = col.number_input("Tasa de decaimiento (lambda)", value=1.0, min_value=0.0)  # Parámetro lambda
        params.append(lambda_)
        
        return params

    elif dist_name == 'Geométrica':
        
        col.write("**Distribución Geométrica**")
        get_latex_formula(dist_name, col)
        p = col.number_input("Probabilidad de éxito (p)", min_value=0.0, max_value=1.0, value=0.5)  # Probabilidad de éxito
        params.append(p)
        
        return params

    elif dist_name == 'Binomial Negativa':
        
        col.write("**Distribución Binomial Negativa**")
        get_latex_formula(dist_name, col)
        r = col.number_input("Número de fracasos (r)", value=10, min_value=1)  # Número de fracasos
        p = col.number_input("Probabilidad de éxito (p)", min_value=0.0, max_value=1.0, value=0.5)  # Probabilidad de éxito
        params.append(r)
        params.append(p)
        
        return params

    elif dist_name == 'Uniforme':
        
        col.write("**Distribución Uniforme**")
        get_latex_formula(dist_name, col)
        a = col.number_input("Límite inferior (a)", value=0.0)  # Límite inferior
        b = col.number_input("Límite superior (b)", value=1.0)  # Límite superior
        params.append(a)
        params.append(b)
        
        return params

    elif dist_name == 'Beta':
        
        col.write("**Distribución Beta**")
        get_latex_formula(dist_name, col)
        alpha = col.number_input("Parámetro alpha", value=2.0, min_value=0.0)  # Parámetro alpha
        beta = col.number_input("Parámetro beta", value=2.0, min_value=0.0)  # Parámetro beta
        params.append(alpha)
        params.append(beta)
        
        return params

    elif dist_name == 'Gamma':
        
        col.write("**Distribución Gamma**")
        get_latex_formula(dist_name, col)
        alpha = col.number_input("Parámetro alpha", value=2.0, min_value=0.0)  # Parámetro alpha
        beta = col.number_input("Tasa (beta)", value=1.0, min_value=0.0)  # Parámetro beta
        params.append(alpha)
        params.append(beta)
        
        return params

    elif dist_name == 'Chi-cuadrado':
        
        col.write("**Distribución Chi-cuadrado**")
        get_latex_formula(dist_name, col)
        k = col.number_input("Grados de libertad (k)", value=2, min_value=1)  # Grados de libertad
        params.append(k)
        
        return params

    elif dist_name == 't de Student':
        
        col.write("**Distribución t de Student**")
        get_latex_formula(dist_name, col)
        df = col.number_input("Grados de libertad (df)", value=10, min_value=1)  # Grados de libertad
        params.append(df)
        
        return params

    elif dist_name == 'Log-Normal':
        
        col.write("**Distribución Log-Normal**")
        get_latex_formula(dist_name, col)
        sigma = col.number_input("Desviación estándar (sigma)", value=1.0, min_value=0.0)  # Desviación estándar
        scale = col.number_input("Escala (mu)", value=0.0)  # Escala o mu
        params.append(sigma)
        params.append(scale)
        
        return params

    elif dist_name == 'Pareto':
        
        col.write("**Distribución Pareto**")
        get_latex_formula(dist_name, col)
        b = col.number_input("Parámetro de forma (b)", value=2.62, min_value=0.0)  # Parámetro de forma
        params.append(b)
        
        return params
    
    elif dist_name == 'Uniforme Discreta':
        
        col.write("**Distribución Uniforme Discreta**")
        get_latex_formula(dist_name, col)
        a = col.number_input("Límite inferior (a)", value=0, step=1)  # Límite inferior
        b = col.number_input("Límite superior (b)", value=10, step=1)  # Límite superior (exclusivo)
        params.append(a)
        params.append(b)
        
        return params
    
    return None

def get_latex_formula(distribution_name, col=st):
    formulas = {
        'Normal': r'X \sim N(\mu, \sigma^2) \quad \text{donde } f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}',
        'Poisson': r'X \sim \text{Poisson}(\lambda) \quad \text{donde } P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}',
        'Bernoulli': r'X \sim \text{Bernoulli}(p) \quad \text{donde } P(X = 1) = p, \quad P(X = 0) = 1 - p',
        'Binomial': r'X \sim \text{Binomial}(n, p) \quad \text{donde } P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}',
        'Exponencial': r'X \sim \text{Exponencial}(\lambda) \quad \text{donde } f(x) = \lambda e^{-\lambda x}',
        'Geométrica': r'X \sim \text{Geométrica}(p) \quad \text{donde } P(X = k) = (1-p)^{k-1} p',
        'Binomial Negativa': r'X \sim \text{Binomial Negativa}(r, p) \quad \text{donde } P(X = k) = \binom{k+r-1}{k} p^r (1-p)^k',
        'Uniforme': r'X \sim \text{Uniforme}(a, b) \quad \text{donde } f(x) = \frac{1}{b - a} \quad \text{para } a \leq x \leq b',
        'Beta': r'X \sim \text{Beta}(\alpha, \beta) \quad \text{donde } f(x) = \frac{x^{\alpha - 1} (1 - x)^{\beta - 1}}{B(\alpha, \beta)}',
        'Gamma': r'X \sim \text{Gamma}(\alpha, \beta) \quad \text{donde } f(x) = \frac{\beta^\alpha x^{\alpha - 1} e^{-\beta x}}{\Gamma(\alpha)}',
        'Chi-cuadrado': r'X \sim \chi^2(k) \quad \text{donde } f(x) = \frac{1}{2^{k/2} \Gamma(k/2)} x^{(k/2) - 1} e^{-x/2}',
        't de Student': r'X \sim t(k) \quad \text{donde } f(x) = \frac{\Gamma(\frac{k+1}{2})}{\sqrt{k\pi} \Gamma(\frac{k}{2})} \left(1 + \frac{x^2}{k}\right)^{-\frac{k+1}{2}}',
        'Log-Normal': r'X \sim \text{Log-Normal}(\mu, \sigma) \quad \text{donde } f(x) = \frac{1}{x\sigma \sqrt{2\pi}} e^{-\frac{(\ln x - \mu)^2}{2\sigma^2}}',
        'Pareto': r'X \sim \text{Pareto}(\alpha, x_m) \quad \text{donde } f(x) = \frac{\alpha x_m^\alpha}{x^{\alpha + 1}} \quad \text{para } x \geq x_m'
    }
    
    # Obtiene la fórmula en LaTeX
    formula = formulas.get(distribution_name, "Distribución no encontrada.")
    
    # Muestra la fórmula en Streamlit
    col.latex(formula)
