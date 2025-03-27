import streamlit as st
#header
st.set_page_config( page_title="UNIT CONVERTER" , page_icon="🔄" , layout="wide")
st.title("UNIT CONVERTER🔄")
st.write("Dont complicate unit conversions from now on just add the value and convert🔁")

#lenght conversions
def convert_lenght(value,convert_from, convert_to):
    conversions={
       "centimeter_millimeter":10,
       "millimeter_centimeter":0.1,
       "centimeter_angstrom":100000000,
       "angstrom_centimeter": 0.00000001,
       "meter_centimeter":100,
       "centimeter_meter":0.01,
       "meter_kilometer":1000,
       "kilometer_meter":0.001,
       "Foot_inch":12,
       "inch_Foot":0.0833,
       #for same values no conversion is required
       "centimeter_centimeter":1,
       "millimeter_millimeter":1,
       "angstrom_angstrom":1,
       "meter_meter":1,
       "kilometer_kilometer":1,
       "Foot_Foot":1,
       "inch_inch":1
       
    }
    
    converting_key= f"{convert_to}_{convert_from}"
    
    if converting_key in conversions:
       conversion = conversions[converting_key]
       return value * conversion
    else:
      return "conversion not supported"

#Temperature conversions 
def convert_temperature (value,convert_from,convert_to):
   conversions={
      "celcius_farenheit" : lambda v:(v*9/5)+32,
      "farenheit_celcius" : lambda v:(v-32)*5/9,
      "celcius_kelvin": lambda v:(v+273),
      "kelvin_celcius": lambda v:(v-273),
      "kelvin_farenheit":lambda v: (v - 273.15) * 9/5 + 32,
      "farenheit_kelvin":lambda v: (v - 32) * 5/9 + 273.15 ,
      #same units no conversion
      "celcius_celcius":lambda v:(v*1),
      "farenheit_farenheit":lambda v:(v*1),
      "kelvin_kelvin":lambda v:(v*1)
      
   }
   converting_key= f"{convert_to}_{convert_from}"
    
   if converting_key in conversions:
       conversion = conversions[converting_key]
       return conversion(value)
   else:
      return "conversion not supported"
   
   
   #streamlit user interface
conversion_type = st.sidebar.selectbox("SELECT CONVERSION TYPE",["lenght","Temperature"])

if conversion_type == "lenght":
   units= ["centimeter","millimeter","angstrom","meter","kilometer","Foot","inch"]
elif conversion_type == "Temperature":
   units = ["celcius","farenheit","kelvin"]

value = st.number_input("Enter your number" )
convert_to = st.selectbox("convert from" ,units)
convert_from = st.selectbox("convert to" ,units)

if st.button("convert"):
   if conversion_type == "lenght":
      result = convert_lenght(value,convert_from,convert_to)
   elif conversion_type =="Temperature":
      result=convert_temperature(value,convert_from,convert_to)  
   st.write(f"converted value: {result}")
   
   #footer
st.markdown("__________________")
st.markdown("🔆🔅Made by Aliza batool🔆🔅")