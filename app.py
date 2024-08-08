import streamlit as st
from PIL import Image
image = Image.open(r'C:\Users\divyb\Downloads\Elite Dev white.png')
st.image(image,caption='image caption"C:\Users\divyb\Downloads\Elite Dev white.png"')
st.title('Title: Hello')
st.header('Header: Hey')
x = st.text_input('Enter your name')
y = st.number_input('Enter amount')
if y > 10000:
    st.write('Greater')
    st.balloons()
else:
    st.write('Smaller')
st.radio('Radio button', options=['yes','no'])
st.checkbox('checkbox')
st.sidebar.title('Side bar : Schemes')
st.sidebar.markdown('Markdown')
st.tabs('jo')
st.toast('welcome')