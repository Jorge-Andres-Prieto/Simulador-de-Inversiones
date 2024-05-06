# Importa Streamlit para construir interfaces de usuario
import streamlit as st

# Importa NumPy para operaciones numéricas
import numpy as np

# Importa matplotlib para generar gráficos
import matplotlib.pyplot as plt

def calcular_inversion(inicial, tasa, años, adicional):
    """
    Calcula el crecimiento de una inversión con interés compuesto y aportes
    adicionales mensuales.

    Args:
        inicial (float): Monto inicial de la inversión.
        tasa (float): Tasa de interés anual en porcentaje.
        años (int): Duración de la inversión en años.
        adicional (float): Aporte adicional mensual a la inversión.

    Returns:
        list: Lista de balances anuales de la inversión.
    """
    balances = [inicial]
    for año in range(1, años + 1):
        final_año = balances[-1] * (1 + tasa / 100) + adicional * 12
        balances.append(final_año)
    return balances

def main():
    """
    Configura y ejecuta la aplicación Streamlit para simular el crecimiento
    de una inversión.

    Args:
        None

    Returns:
        None
    """
    # Aplica configuraciones iniciales a la página de Streamlit
    st.set_page_config(page_title="Simulador de Inversiones 📈", page_icon="💹")

    # Aplica CSS personalizado para el estilo de la aplicación
    st.markdown("""
        <style>
        .stApp {
            background-color: #55bbc9;
            color: #333333;
        }
        </style>
        """, unsafe_allow_html=True)

    # Título de la aplicación
    st.title('Simulador de Inversiones 🌱')

    # Entradas de usuario para configurar los parámetros de la simulación
    cantidad_inicial = st.number_input(
        'Cantidad inicial 💵 (en dólares)', min_value=0.0, value=1000.0, step=500.0)
    tasa_interes = st.number_input(
        'Tasa de interés anual (%) 📊', min_value=0.0, value=5.0, step=0.1)
    años = st.number_input(
        'Número de años 🗓️', min_value=1, max_value=50, value=10, step=1)
    aporte_mensual = st.number_input(
        'Aporte mensual adicional 💰 (en dólares)', min_value=0.0, value=100.0, step=50.0)

    # Botón para ejecutar la simulación
    if st.button('Calcular 🧮'):
        # Calcula los balances de la inversión a lo largo de los años
        balances = calcular_inversion(
            cantidad_inicial, tasa_interes, años, aporte_mensual)

        # Muestra el balance final después del período de inversión
        st.write(f"Balance final después de {años} años: ${balances[-1]:,.2f}")

        # Grafica los resultados de la inversión
        fig, ax = plt.subplots()
        ax.plot(range(años + 1), balances, marker='o', color="#35b995")
        ax.set_title("Crecimiento de la Inversión 📈")
        ax.set_xlabel("Años")
        ax.set_ylabel("Balance ($)")
        ax.grid(True)
        st.pyplot(fig)

if __name__ == "__main__":
    main()
