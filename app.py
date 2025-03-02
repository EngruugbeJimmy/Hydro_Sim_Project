import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from hydro_model import hydro_model

st.title("Hydrodynamic Simulation 🌊")
st.sidebar.header("Simulation Parameters")

L = st.sidebar.slider("Channel Length (m)", 5, 50, 10)
nx = st.sidebar.slider("Grid Points", 50, 200, 100)
T = st.sidebar.slider("Simulation Time (s)", 5, 100, 30)
dt = st.sidebar.slider("Time Step Size (s)", 0.01, 0.1, 0.01)
R = st.sidebar.slider("Rainfall Intensity (m/s)", 10.0, 0.0, 0.01, 0.001)

if st.sidebar.button("Run Simulation"):
    x, t, h = hydro_model(L, nx, T, dt, R)

    st.success("Simulation Completed Successfully!")
    
    # 2D Plot
    st.subheader("Water Depth Evolution")
    plt.figure(figsize=(10, 6))
    for i in range(0, len(t), len(t)//10):
        plt.plot(x, h[i], label=f"t={t[i]:.2f}s")
    plt.xlabel("Distance (m)")
    plt.ylabel("Water Depth (m)")
    plt.legend()
    st.pyplot(plt)

    # 3D Plot
    st.subheader("3D Visualization")
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    X, T = np.meshgrid(x, t)
    ax.plot_surface(X, T, h, cmap='viridis')
    ax.set_xlabel('Distance (m)')
    ax.set_ylabel('Time (s)')
    ax.set_zlabel('Water Depth (m)')
    st.pyplot(fig)
