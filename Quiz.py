import streamlit as st

st.write('Hello, I am Sumit, Welcome to my quiz Zone.. Hope you like the game. You may please Proceed further for gaming...')
age = st.number_input('Enter ur Age....')
if age>= 18:
  st.write("You are eligible for License...")
  st.balloons()
  # st.snow()
  st.toast("Elligbile")
else:
  st.write('You are not eligible...')
  
