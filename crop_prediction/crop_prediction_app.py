# Import necessary libraries
import streamlit as st
import pickle as pk

# Streamlit app header/title
st.title('Crop Type Prediction App')

# Add a sidebar for user input
st.sidebar.header('Input Features')

# Create input fields for user to input data
nitrogen = st.sidebar.slider('Nitrogen Level', min_value=0.0, max_value=100.0, value=50.0)
phosphorus = st.sidebar.slider('Phosphorus Level', min_value=0.0, max_value=100.0, value=50.0)
potassium = st.sidebar.slider('Potassium Level', min_value=0.0, max_value=100.0, value=50.0)
temperature = st.sidebar.slider('Temperature (°C)', min_value=0.0, max_value=40.0, value=25.0)
humidity = st.sidebar.slider('Humidity (%)', min_value=0, max_value=100, value=50)
ph = st.sidebar.slider('pH Level', min_value=0.0, max_value=14.0, value=7.0)
rainfall = st.sidebar.slider('Rainfall (mm)', min_value=0.0, max_value=300.0, value=150.0)

# Define the crop mapping dictionary
crop_mapping = {
    0: 'rice',
    1: 'maize',
    2: 'chickpea',
    3: 'kidneybeans',
    4: 'pigeonpeas',
    5: 'mothbeans',
    6: 'mungbean',
    7: 'blackgram',
    8: 'lentil',
    9: 'pomegranate',
    10: 'banana',
    11: 'mango',
    12: 'grapes',
    13: 'watermelon',
    14: 'muskmelon',
    15: 'apple',
    16: 'orange',
    17: 'papaya',
    18: 'coconut',
    19: 'cotton',
    20: 'jute',
    21: 'coffee'
}

# Create a button to trigger prediction
if st.sidebar.button('Predict'):
    # Prepare input data for prediction
    input_data = [[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]]
    with open('cropab_Decision.pkl','rb') as file:
        clf = pk.load(file)
    predicted_crop = clf.predict(input_data)
    
    # Map the predicted value to crop name
    if predicted_crop[0] in crop_mapping:
        predicted_crop_name = crop_mapping[predicted_crop[0]]
        st.subheader(f'Predicted Crop Type: {predicted_crop_name}')
    else:
        st.subheader('Crop Type not found in mapping')
