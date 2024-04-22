import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def calcular_inversion(inicial, tasa, años, adicional):
    # Calcula el balance anual de la inversión con interés compuesto y aportes adicionales mensuales
    balances = [inicial]
    for año in range(1, años + 1):
        final_año = balances[-1] * (1 + tasa / 100) + adicional * 12
        balances.append(final_año)
    return balances

def main():
    # Aplicar el tema personalizado
    st.set_page_config(page_title="Simulador de Inversiones 📈", page_icon="💹")
    st.markdown("""
        <style>
        .stApp {
            background-color: #55bbc9;
            color: #333333;
        }
        </style>
        """, unsafe_allow_html=True)

    st.title('Simulador de Inversiones 🌱')

    # Entradas del usuario
    cantidad_inicial = st.number_input('Cantidad inicial 💵 (en dólares)', min_value=0.0, value=1000.0, step=500.0)
    tasa_interes = st.number_input('Tasa de interés anual (%) 📊', min_value=0.0, value=5.0, step=0.1)
    años = st.number_input('Número de años 🗓️', min_value=1, max_value=50, value=10, step=1)
    aporte_mensual = st.number_input('Aporte mensual adicional 💰 (en dólares)', min_value=0.0, value=100.0, step=50.0)

    if st.button('Calcular 🧮'):
        # Procesamiento de los datos
        balances = calcular_inversion(cantidad_inicial, tasa_interes, años, aporte_mensual)

        # Mostrar resultados
        st.write(f"Balance final después de {años} años: ${balances[-1]:,.2f}")

        # Graficar los resultados
        fig, ax = plt.subplots()
        ax.plot(range(años + 1), balances, marker='o', color="#35b995")
        ax.set_title("Crecimiento de la Inversión 📈")
        ax.set_xlabel("Años")
        ax.set_ylabel("Balance ($)")
        ax.grid(True)
        st.pyplot(fig)

if __name__ == "__main__":
    main()
