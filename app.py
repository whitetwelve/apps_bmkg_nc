import joblib
import pandas as pd
import streamlit as st

# Load the model
model = joblib.load('fuad.sav')

# Daftar Kabupaten
daftar_kabupaten = [
    "BANDUNG", "BANDUNG BARAT", "BANGKALAN", "BANJARNEGARA", "BANTUL", "BANYUMAS", "BANYUWANGI",
    "BATANG", "BLITAR", "BLORA", "BOGOR", "BONDOWOSO", "BOYOLALI", "BREBES", "CIAMIS", "CIANJUR",
    "CILACAP", "DEMAK", "GARUT", "GRESIK", "GROBOGAN", "GUNUNG KIDUL", "INDRAMAYU", "JEMBER", "JEPARA",
    "JOMBANG", "KARANGANYAR", "KARAWANG", "KEBUMEN", "KENDAL", "KOTA MALANG", "KUNINGAN", "LAMONGAN",
    "LAMPUNG SELATAN", "LAMPUNG TENGAH", "LAMPUNG TIMUR", "LEBAK", "LUMAJANG", "MADIUN", "MAGELANG",
    "MAJALENGKA", "MALANG", "MOJOKERTO", "NGANJUK", "NGAWI", "PACITAN", "PAMEKASAN", "PANDEGLANG",
    "PANGANDARAN", "PATI", "PEKALONGAN", "PEMALANG", "PESAWARAN", "PONOROGO", "PROBOLINGGO", "PURWAKARTA",
    "SAMPANG", "SIDOARJO", "SRAGEN", "SUBANG", "SUKABUMI", "SUMEDANG", "SUMENEP", "TASIKMALAYA", "TEGAL",
    "TRENGGALEK", "TUBAN", "TULUNGAGUNG", "WONOGIRI", "WONOSOBO"
]

# Function to make prediction
def predict_precipitation(d2m, e, t2m, r, ws, kabupaten):
    input_data = pd.DataFrame({
        'd2m': [d2m],
        'e': [e],
        't2m': [t2m],
        'r': [r],
        'ws': [ws],
        'KABUPATEN': [daftar_kabupaten.index(kabupaten)]
    })
    predicted_precip = model.predict(input_data)
    return predicted_precip[0]

# Function to classify precipitation type
def classify_precipitation(predicted_precip):
    if predicted_precip >= 0 and predicted_precip <= 0.50:
        return "Berawan"
    elif predicted_precip > 0.50 and predicted_precip <= 200:
        return "Hujan Ringan (Hijau)"
    elif predicted_precip > 200 and predicted_precip <= 500:
        return "Hujan Sedang (Kuning)"
    elif predicted_precip > 500 and predicted_precip <= 1000:
        return "Hujan Lebat (Oranye)"
    elif predicted_precip > 1000 and predicted_precip <= 1500:
        return "Hujan Sangat Lebat (Merah)"
    else:
        return "Hujan Ekstrem (Ungu)"

# Streamlit app
def main():
    st.title('Prediksi Curah Hujan Kabupaten di Jawa')

    # Input parameters
    d2m = st.slider('Suhu titik embun', min_value=0.0, max_value=30.0, value=20.0, step=0.1)
    e = st.slider('Evaporasi', min_value=0.0, max_value=10.0, value=3.0, step=0.1)
    t2m = st.slider('Suhu', min_value=0.0, max_value=40.0, value=22.0, step=0.1)
    r = st.slider('Kelembapan', min_value=0.0, max_value=100.0, value=50.0, step=0.1)
    ws = st.slider('Kecepatan Angin', min_value=0.0, max_value=2.0, value=0.5, step=0.01)
    kabupaten = st.selectbox('KABUPATEN', daftar_kabupaten)

    # Make prediction
    if st.button('Predict'):
        predicted_precip = predict_precipitation(d2m, e, t2m, r, ws, kabupaten)
        precipitation_type = classify_precipitation(predicted_precip)
         # Menambahkan enter pada output
        st.success(f'Prediksi Curah Hujan untuk kabupaten {kabupaten}: {predicted_precip:.2f} mm')
        st.success(f'Jenis Curah Hujan: {precipitation_type}')
if __name__ == '__main__':
    
    main()
