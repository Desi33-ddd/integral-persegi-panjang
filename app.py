# app.py

import streamlit as st
import numpy as np

# --- Judul Aplikasi ---
st.title("🔢 Solusi Integral Numerik")
st.header("Kaidah Pias Persegi Panjang (Riemann)")

st.sidebar.title("Pengaturan Integral")

# --- Input Fungsi ---
st.sidebar.write("Definisikan fungsi f(x):")
# Catatan: Fungsi ini perlu diubah menjadi string evaluasi yang aman jika fungsi kompleks digunakan.
# Untuk saat ini, kita akan menggunakan fungsi sederhana
fungsi_str = st.sidebar.text_input("f(x) (contoh: x**2 + 2*x)", value="x**2")

try:
    # Fungsi yang akan diintegralkan
    # Menggunakan lambda untuk mengevaluasi fungsi dari input string
    f = lambda x: eval(fungsi_str) 
except:
    st.error("Format fungsi tidak valid. Pastikan format Python yang benar (misalnya: x**2, np.sin(x)).")
    st.stop()


# --- Input Batas dan Pias ---
a = st.sidebar.number_input("Batas bawah (a)", value=0.0)
b = st.sidebar.number_input("Batas atas (b)", value=1.0)
n = st.sidebar.slider("Jumlah Pias (n)", min_value=10, max_value=1000, value=100)

# --- Implementasi Kaidah Persegi Panjang Kiri ---
def integral_persegi_panjang(f, a, b, n):
    """Menghitung integral menggunakan kaidah persegi panjang (sisi kiri)."""
    if a >= b:
        st.warning("Batas bawah (a) harus lebih kecil dari batas atas (b).")
        return 0.0

    h = (b - a) / n  # Lebar setiap pias
    integral = 0.0
    
    # Hitung luas untuk setiap pias (menggunakan tinggi di sisi kiri pias)
    for i in range(n):
        x_i = a + i * h
        integral += f(x_i)
        
    integral *= h
    return integral

# --- Tampilan Hasil ---
if st.sidebar.button("Hitung Integral"):
    hasil = integral_persegi_panjang(f, a, b, n)
    
    st.success(f"✅ **Hasil Integral:** {hasil}")
    st.info(f"Dihitung untuk fungsi $f(x) = {fungsi_str}$ dari $x={a}$ sampai $x={b}$ menggunakan $n={n}$ pias.")
    
    # --- Tampilan Visualisasi (Sederhana) ---
    st.subheader("Visualisasi")
    
    # Membuat data untuk plotting
    x_vals = np.linspace(a, b, 500)
    y_vals = [f(x) for x in x_vals]
    
    data = {'x': x_vals, 'y': y_vals}
    st.line_chart(data, x='x', y='y')
    
    st.caption("Grafik fungsi f(x) yang diintegralkan.")


# --- Catatan Penting untuk Deploy ---
st.markdown("---")
st.markdown(
    """
    **Catatan untuk Deployment:** Pastikan Anda juga memiliki file `requirements.txt` 
    yang berisi library yang digunakan (minimal: `streamlit`, `numpy`).
    """
)
