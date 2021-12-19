import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from streamlit_drawable_canvas import st_canvas


title = "Pywritings : ___Python___ detect ___writings___"
sidebar_name = "Try out the algorithm"

def run():

    st.title(title)

    option = st.selectbox(
        'What would you like to pywrite?',
        ('Png file', 'Handwriting'))

    st.write('You selected:', option)

    if 'Png file' in option:
        uploaded_files = st.file_uploader("Choose jpg file", accept_multiple_files=True)
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            st.write("filename:", uploaded_file.name)
            st.write(bytes_data)
            uploaded_files = st.file_uploader("Choose jpg file", accept_multiple_files=True)

    if 'Handwriting' in option:
        st.markdown("""
        Draw your text on the canvas.
        """)
        # Specify brush parameters and drawing mode
        b_width: int = 20
        bg_color = "#FFFFFF"
        # bg_color = st.sidebar.beta_color_picker("Enter background color hex: ", "#eee")
        # drawing_mode = st.sidebar.checkbox("Drawing mode ?", True)

        # Create a canvas component
        image_data = st_canvas(
            b_width, stroke_width=5, height=200, width=900, key="canvas"
        )
