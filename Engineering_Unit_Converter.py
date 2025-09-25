import streamlit as st

import streamlit as st

import streamlit as st

# ------------------ Converter Functions ------------------

def length_converter(value, from_unit, to_unit):
    units = {"m":1, "cm":0.01, "mm":0.001, "in":0.0254, "ft":0.3048}
    return value * units[from_unit] / units[to_unit]

def mass_converter(value, from_unit, to_unit):
    units = {"kg":1, "g":0.001, "lb":0.453592, "ton":1000}
    return value * units[from_unit] / units[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "C" and to_unit == "K":
        return value + 273.15
    elif from_unit == "K" and to_unit == "C":
        return value - 273.15
    elif from_unit == "C" and to_unit == "F":
        return (value * 9/5) + 32
    elif from_unit == "F" and to_unit == "C":
        return (value - 32) * 5/9
    elif from_unit == "K" and to_unit == "F":
        return (value - 273.15) * 9/5 + 32
    elif from_unit == "F" and to_unit == "K":
        return (value - 32) * 5/9 + 273.15
    else:
        return value

def force_converter(value, from_unit, to_unit):
    units = {"N":1, "kN":1000, "lbf":4.44822}
    return value * units[from_unit] / units[to_unit]

def pressure_converter(value, from_unit, to_unit):
    units = {"Pa":1, "bar":1e5, "atm":101325, "psi":6894.76}
    return value * units[from_unit] / units[to_unit]

def energy_converter(value, from_unit, to_unit):
    units = {"J":1, "kJ":1000, "cal":4.184, "kWh":3.6e6, "BTU":1055.06}
    return value * units[from_unit] / units[to_unit]

def power_converter(value, from_unit, to_unit):
    units = {"W":1, "kW":1000, "MW":1e6, "hp":745.7}
    return value * units[from_unit] / units[to_unit]

def torque_converter(value, from_unit, to_unit):
    units = {"Nm":1, "kNm":1000, "lbft":1.35582}
    return value * units[from_unit] / units[to_unit]


# ------------------ Streamlit UI ------------------

st.set_page_config(page_title="Engineering Unit Converter", page_icon="⚙️", layout="centered")

st.title("⚙️ Engineering Unit Converter")
st.markdown("Convert between common **engineering units** (Length, Mass, Force, Pressure, Energy, Power, Torque, Temperature).")

# Dropdown for type
quantity = st.selectbox("Choose Quantity Type:", 
    ["Length", "Mass", "Temperature", "Force", "Pressure", "Energy", "Power", "Torque"])

# Input value
value = st.number_input("Enter value to convert:", value=1.0)

# Select units
if quantity == "Length":
    from_unit = st.selectbox("From Unit", ["m", "cm", "mm", "in", "ft"])
    to_unit = st.selectbox("To Unit", ["m", "cm", "mm", "in", "ft"])
    result = length_converter(value, from_unit, to_unit)

elif quantity == "Mass":
    from_unit = st.selectbox("From Unit", ["kg", "g", "lb", "ton"])
    to_unit = st.selectbox("To Unit", ["kg", "g", "lb", "ton"])
    result = mass_converter(value, from_unit, to_unit)

elif quantity == "Temperature":
    from_unit = st.selectbox("From Unit", ["C", "K", "F"])
    to_unit = st.selectbox("To Unit", ["C", "K", "F"])
    result = temperature_converter(value, from_unit, to_unit)

elif quantity == "Force":
    from_unit = st.selectbox("From Unit", ["N", "kN", "lbf"])
    to_unit = st.selectbox("To Unit", ["N", "kN", "lbf"])
    result = force_converter(value, from_unit, to_unit)

elif quantity == "Pressure":
    from_unit = st.selectbox("From Unit", ["Pa", "bar", "atm", "psi"])
    to_unit = st.selectbox("To Unit", ["Pa", "bar", "atm", "psi"])
    result = pressure_converter(value, from_unit, to_unit)

elif quantity == "Energy":
    from_unit = st.selectbox("From Unit", ["J", "kJ", "cal", "kWh", "BTU"])
    to_unit = st.selectbox("To Unit", ["J", "kJ", "cal", "kWh", "BTU"])
    result = energy_converter(value, from_unit, to_unit)

elif quantity == "Power":
    from_unit = st.selectbox("From Unit", ["W", "kW", "MW", "hp"])
    to_unit = st.selectbox("To Unit", ["W", "kW", "MW", "hp"])
    result = power_converter(value, from_unit, to_unit)

elif quantity == "Torque":
    from_unit = st.selectbox("From Unit", ["Nm", "kNm", "lbft"])
    to_unit = st.selectbox("To Unit", ["Nm", "kNm", "lbft"])
    result = torque_converter(value, from_unit, to_unit)


# Display result
st.success(f"✅ {value} {from_unit} = {result:.3f} {to_unit}")
