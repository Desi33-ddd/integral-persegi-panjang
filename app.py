import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Aplikasi Integral - Kaidah Pias Persegi Panjang")

fungsi_input = st.text_input("Masukkan fungsi f(x):", "x**2")

a = st.number_input("Batas bawah (a):", value=0.0)
b = st.number_input("Batas atas (b):", value=5.0)

n = st.slider("Jumlah Pias (n):", 1, 200, 10)

def f(x):
    return eval(fungsi_input)

dx = (b - a) / n

x_plot = np.linspace(a, b, 1000)
y_plot = f(x_plot)

x_i = np.linspace(a, b-dx, n)
y_i = f(x_i)

integral = np.sum(y_i * dx)

st.write(f"**Hasil Integral (Riemann Kiri) = {integral:.4f}**")

fig, ax = plt.subplots()
ax.plot(x_plot, y_plot, label="f(x)")

for i in range(n):
    ax.bar(x_i[i], y_i[i], width=dx, alpha=0.3, align='edge')

st.pyplot(fig)
