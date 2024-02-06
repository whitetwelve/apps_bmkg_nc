import streamlit as st
import pickle
import pandas as pd

# Load the XGBoost model
filename = 'model.sav'
try:
    model = pickle.load(open(filename, 'rb'))
    st.sidebar.success("Model loaded successfully.")
except Exception as e:
    st.sidebar.error(f"Error loading the model: {e}")

# Function to predict precipitation
def predict_precipitation(input_data):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)
    return prediction[0]
st.title('Prediksi Tingkat Curah Hujan')
# Streamlit app
def main():
    

    # Input form
    st.sidebar.header('Input Data')
e = st.sidebar.slider('Evaporasi', min_value=0.0, max_value=100.0, value=38.3)
d2m = st.sidebar.slider('Suhu titik embun', min_value=0.0, max_value=50.0, value=24.2)
t2m = st.sidebar.slider('Suhu', min_value=0.0, max_value=35.0, value=24.0)
r = st.sidebar.slider('Kelembapan', min_value=0, max_value=100, value=75)
ws = st.sidebar.slider('Angin', min_value=0, max_value=100, value=49)
kabupaten = st.sidebar.selectbox('KABUPATEN', [
    "BANDUNG", "BANDUNG BARAT", "BANGKALAN", "BANJARNEGARA", "BANTUL", "BANYUMAS", "BANYUWANGI",
    "BATANG", "BLITAR", "BLORA", "BOGOR", "BONDOWOSO", "BOYOLALI", "BREBES", "CIAMIS", "CIANJUR",
    "CILACAP", "DEMAK", "GARUT", "GRESIK", "GROBOGAN", "GUNUNG KIDUL", "INDRAMAYU", "JEMBER", "JEPARA",
    "JOMBANG", "KARANGANYAR", "KARAWANG", "KEBUMEN", "KENDAL", "KOTA MALANG", "KUNINGAN", "LAMONGAN",
    "LAMPUNG SELATAN", "LAMPUNG TENGAH", "LAMPUNG TIMUR", "LEBAK", "LUMAJANG", "MADIUN", "MAGELANG",
    "MAJALENGKA", "MALANG", "MOJOKERTO", "NGANJUK", "NGAWI", "PACITAN", "PAMEKASAN", "PANDEGLANG",
    "PANGANDARAN", "PATI", "PEKALONGAN", "PEMALANG", "PESAWARAN", "PONOROGO", "PROBOLINGGO", "PURWAKARTA",
    "SAMPANG", "SIDOARJO", "SRAGEN", "SUBANG", "SUKABUMI", "SUMEDANG", "SUMENEP", "TASIKMALAYA", "TEGAL",
    "TRENGGALEK", "TUBAN", "TULUNGAGUNG", "WONOGIRI", "WONOSOBO"
])

input_data = {
        'e': e,
        'd2m': d2m,
}

    # Predict button
if st.sidebar.button('Prediksi'):
    result = predict_precipitation(input_data)

    if result == 0 or (0 < result < 0.5):
        category = "Berawan"
    elif 0.5 <= result < 20:
        category = "Hujan Ringan"
    elif 20 <= result < 50:
        category = "Hujan Sedang"
    elif 50 <= result < 100:
        category = "Hujan Lebat"
    elif 100 <= result < 150:
        category = "Hujan Sangat Lebat"
    elif result >= 150:
        category = "Hujan Ekstrem"
    else:
        category = "Uncategorized"

    # Display the result with specific formatting
    st.markdown(f'**Prediksi Precipitation:** {category}', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
