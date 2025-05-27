import streamlit as st
st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis Sebuah Angka:", value=0, step=1)

if(angka%2)==0:
    st.writer(f"{angka}adalah Bilangam Genap") 
else:
    st.writer(f"{angka} adalah Bilangan Ganjil")


