import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from modelo import resolver_optimizacion

# Configuración de la interfaz
st.set_page_config(page_title="Optimizador de Paneles Solares", layout="wide")

st.title("☀️ Optimizador de Inversión en Paneles Solares")
st.markdown("""
Esta herramienta utiliza un modelo de programación lineal para encontrar la combinación de paneles 
más económica que satisfaga sus necesidades energéticas.
""")

# Sidebar: Entradas de usuario
st.sidebar.header("Parámetros de Entrada")
casa = st.sidebar.selectbox("Seleccione un perfil de casa:", ["Casa 1", "Casa 2", "Casa 3", "Manual"])

# Valores por defecto basados en los datos recolectados (Tarea 1)
if casa == "Casa 1":
    area_def, cons_def = 150.0, 445.0
elif casa == "Casa 2":
    area_def, cons_def = 188.0, 404.0
elif casa == "Casa 3":
    area_def, cons_def = 228.0, 125.0
else:
    area_def, cons_def = 100.0, 200.0

area_disponible = st.sidebar.number_input("Área de techo disponible (m²)", value=area_def)
consumo_requerido = st.sidebar.number_input("Consumo mensual (kWh/mes)", value=cons_def)
horas_sol = st.sidebar.slider("Horas pico solar por día", 3.0, 6.0, 4.5)

# Botón para ejecutar el modelo
if st.button("Calcular Solución Óptima"):
    res = resolver_optimizacion(area_disponible, consumo_requerido, horas_sol)
    
    if res["status"] == "Optimal":
        st.success("✅ ¡Solución Óptima Encontrada!")
        
        # Métricas principales
        m1, m2, m3 = st.columns(3)
        m1.metric("Inversión Total", f"${res['costo']:,.2f}")
        m2.metric("Paneles Totales", int(res['total_paneles']))
        m3.metric("Espacio Usado", f"{res['area_usada']:.2f} m²")
        
        # Gráfico de barras de paneles
        st.subheader("Distribución de Paneles")
        fig, ax = plt.subplots(figsize=(8, 4))
        tipos = ['Panel A', 'Panel B', 'Panel C']
        cantidades = [res['x'], res['y'], res['z']]
        ax.bar(tipos, cantidades, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
        ax.set_ylabel('Cantidad')
        st.pyplot(fig)
        
        # Interpretación Gerencial
        st.subheader("📝 Interpretación Gerencial")
        porcentaje_techo = (res['area_usada'] / area_disponible) * 100
        st.info(f"""
        Para cubrir un consumo de {consumo_requerido} kWh/mes, se recomienda la instalación de 
        {int(res['x'])} unidades de Panel A, {int(res['y'])} de Panel B y {int(res['z'])} de Panel C. 
        
        El proyecto es financieramente óptimo con una inversión de ${res['costo']:,.2f}. 
        Físicamente es viable, ya que solo ocupa el {porcentaje_techo:.1f}% del área disponible del techo.
        """)
    else:
        st.error("❌ El modelo no tiene solución. Verifique que el área del techo sea suficiente para el consumo solicitado.")
