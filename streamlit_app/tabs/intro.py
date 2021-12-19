import streamlit as st


title = "Pywritings : ___Python___ detect ___writings___"
sidebar_name = "Welcome Pywriter"


def run():

    # TODO: choose between one of these GIFs
    # st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/1.gif")
    # st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/2.gif")
    st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/3.gif")

    st.title(title)

    st.markdown("---")

    st.markdown(
        """
    Optical Character Recognition is the field of extracting text from an image to be manipulated by the computer. Although paper is a natural means of communication for humans, it is not understandable by a computer, so many insurance companies are interested in this type of tool to identify their handwritten documents (birth certificate, bill of sale, etc.).
    The objective of this app is to use a deep learning algorithm (computer vision) to recognise characters in pdf/png files that you can download.
    
    The Data is from IAM Handwriting Database 3.0 and contains :
    - 657 people participated in handwriting files 
    - 1,539 pages of scanned text
    - 5,685 isolated and labelled sentences
    - 13,353 isolated and labelled lines of text
    - 115,320 isolated and labelled words
    
    The data are available [here](http://www.fki.inf.unibe.ch/databases/iam-handwriting-database).
        """
    )
