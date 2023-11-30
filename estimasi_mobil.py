import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi mobil bekas')

year = st.number_input('Input tahun mobil')
mileage = st.number_input('input km mobil')
tax = st.number_input('input pajak mobil')
mpg = st.number_input('input konsumsi BBM mobil')
engineSize = st.number_input('input engine size')

predict = ''

if st.button('Estimasi harga'):
    predict = model.predict(
        [[year,mileage,tax,mpg,engineSize]]
    )
    st.write('Estimasi harga mobil bekas dalam POUNDS : ', predict)
    st.write('Estimasi harga mobil bekas dalam IDR (Juta) : ', predict*19677)
