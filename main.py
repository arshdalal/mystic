from PIL import Image
import streamlit as st
with st.container():
    st.subheader('Made by: Arsh Dalal :wave:')
    st.title('Mystic Hallow Webpage')
    st.write('Created using python and streamlit')

my_image = Image.open("C:/Users/arsha/Downloads/Mystic_Hallow.png")

st.image(my_image)

with st.container():
    st.write('###')
    st.write('---')
    st.subheader('First person POV of the Mystic Hallow ride!')
    st.write(
        'This video shows a first person perspective of how going on the mystic hallow will look like, '
        'as well as the speed of the ride!'
    )

my_image2 = Image.open("C:/Users/arsha/OneDrive/Desktop/Roller_thumbnail.jpg")
st.image(my_image2)
st.write('[Video Link ->](https://www.youtube.com/watch?v=c1s9S0EIQLM&ab_channel=Shshhsjdj)')
st.write('###')
st.write('---')
