#project 01 unit converter
# Build unit convertor using python and streamlit

import streamlit as st  

st.markdown(
    """
    <style>
    body{
        background-color: #909097;
        color:white;
    }
    .stApp{
        background-color: linear-gradient(to right, #D7BDE2, #D8D8D8);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.5);
    }
    h1{
        text-align: center;
        font-size: 30px;
        color: white;
    }
    .stButton>button{
        background-color: linear-gradient(45deg, #283593, #7D3C98);
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: background-color 0.3s ease;
        box-shadow: 0px 4px 10px rgba(0, 201, 255, 0.4);
    }
    .stButton>button:hover{
        transform: scale(1.05);
        background: linear-gradient(45deg, #7d3c98, #6c3483);
        box-shadow: 0px 4px 10px rgba(241, 148, 138, 0.4);
        color: black;
    }
    .result-box{
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
    }
    .footer{
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: black;
        
    }
    </style>
    """,
    unsafe_allow_html=True
)
# title and Description
st.markdown("<h1> Unit Converter</h1>", unsafe_allow_html=True)
st.write("Convert between different units of measurement")

# sidebar menue
converion_type = st.sidebar.selectbox("choose conversion type", ["length", "weight","temperature", "volume", "Pressure"])
value = st.number_input("enter the value", value=0.0, min_value=0.0, step=0.1) 
col1, col2 = st.columns(2)

if converion_type == "length":
    with col1:
        from_unit = st.selectbox("from",["meter", "kilometer", "mile", "yard", "foot", "inch", "millimeter", "centimeter"])
    with col2:
        to_unit = st.selectbox("to",["meter", "kilometer", "mile", "yard", "foot", "inch", "millimeter", "centimeter"])
elif converion_type == "weight":
    with col1:
        from_unit = st.selectbox("from", ["kilogram", "gram", "milligram", "pound", "ounce"])     
    with col2:
        to_unit = st.selectbox("to", ["kilogram", "gram", "milligram", "pound", "ounce"])
elif converion_type == "temperature":
    with col1:
        from_unit = st.selectbox("from", ["celsius", "fahrenheit", "kelvin"])   
    with col2:
        to_unit = st.selectbox("to", ["celsius", "fahrenheit", "kelvin"])
elif converion_type == "volume":
    with col1:
        from_unit = st.selectbox("from", ["liter", "milliliter", "gallon", "cup", "pint", "quart", "tablespoon", "teaspoon"])   
    with col2:
        to_unit = st.selectbox("to", ["liter", "milliliter", "gallon", "cup", "pint", "quart", "tablespoon", "teaspoon"])
elif converion_type == "Pressure":
    with col1:
        from_unit = st.selectbox("from", ["bar", "psi", "atmosphere", "torr", "pascal"])
    with col2:
        to_unit = st.selectbox("to", ["bar", "psi", "atmosphere", "torr", "pascal"])


#converted function
def lenght_convertor(value, from_unit, to_unit):
    length_units = {
        "meter": 1.0,
        "kilometer": 1000,
        "mile": 1609.34,
        "yard": 1.09361,
        "foot": 3.28084,    
        "inch": 39.3701,
        "millimeter": 1000,
        "centimeter": 100,
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_convertor(value, from_unit, to_unit):
    weight_units = {
        "kilogram": 1.0,
        "gram": 1000,
        "milligram": 1000000,
        "pound": 2.20462,
        "ounce": 35.274,
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temperature_convertor(value, from_unit, to_unit):
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "celsius" and to_unit == "kelvin":
        return value + 273.15   
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9
    elif from_unit == "fahrenheit" and to_unit == "kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin" and to_unit == "celsius":
        return value - 273.15
    elif from_unit == "kelvin" and to_unit == "fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return value    
    
def volume_convertor(value, from_unit, to_unit):
    volume_units = {
        "liter": 1.0,
        "milliliter": 1000,
        "gallon": 3.78541,
        "cup": 0.236588,
        "pint": 0.473176,
        "quart": 0.946353,
        "tablespoon": 0.0147868,
        "teaspoon": 0.0443603,
    }
    return (value / volume_units[from_unit]) * volume_units[to_unit]

def pressure_convertor(value, from_unit, to_unit):
    pressure_units = {
        "bar": 1.0,
        "psi": 14.5038,
        "atmosphere": 1.01325,
        "torr": 750.062,
        "pascal": 100000,
    }
    return (value / pressure_units[from_unit]) * pressure_units[to_unit]

#Button for conversion
if st.button("📅convert"):
    if converion_type == "length":
        result = lenght_convertor(value, from_unit, to_unit)
    elif converion_type == "weight":
        result = weight_convertor(value, from_unit, to_unit)
    elif converion_type == "temperature":
        result = temperature_convertor(value, from_unit, to_unit)
    elif converion_type == "volume":
        result = volume_convertor(value, from_unit, to_unit)
    elif converion_type == "Pressure":
        result = pressure_convertor(value, from_unit, to_unit)
    #Display the result
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.2f} {to_unit}</div>", unsafe_allow_html=True)
    
    #footer
    st.markdown("<div class='footer'>Developed by Muhammad Tahir Ilyas <a href='https://github.com/Tahir-ilyas'></a></div>", unsafe_allow_html=True)

        
    







