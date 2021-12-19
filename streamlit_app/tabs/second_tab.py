import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

title = "Pywritings : ___Python___ detect ___writings___"
sidebar_name = "What does OCR mean ?"


def run():
    st.title(title)

    st.markdown(
        """
            Optical character recognition or optical character reader (OCR) is the electronic or mechanical conversion of images of typed, handwritten or printed text into machine-encoded text, whether from a scanned document, a photo of a document, a scene-photo (for example the text on signs and billboards in a landscape photo) or from subtitle text superimposed on an image (for example: from a television broadcast).

    Widely used as a form of data entry from printed paper data records – whether passport documents, invoices, bank statements, computerized receipts, business cards, mail, printouts of static-data, or any suitable documentation – it is a common method of digitizing printed texts so that they can be electronically edited, searched, stored more compactly, displayed on-line, and used in machine processes such as cognitive computing, machine translation, (extracted) text-to-speech, key data and text mining. OCR is a field of research in pattern recognition, artificial intelligence and computer vision.
    """
    )

    col2, col3 = st.columns(2)
    with col2:
        st.markdown(
            """
        ## Some OCR applications

        OCR engines have been developed into many kinds of domain-specific OCR applications, such as receipt OCR, invoice OCR, check OCR, legal billing document OCR.

        They can be used for:
        - Data entry for business documents, e.g. Cheque, passport, invoice, bank statement and receipt
        - Automatic number plate recognition
        - In airports, for passport recognition and information extraction
        - Automatic insurance documents key information extraction[citation needed]
        - Traffic sign recognition
        - Extracting business card information into a contact list
        - More quickly make textual versions of printed documents, e.g. book scanning for Project Gutenberg
        - Make electronic images of printed documents searchable, e.g. Google Books
        - Converting handwriting in real-time to control a computer (pen computing)
        - Defeating CAPTCHA anti-bot systems, though these are specifically designed to prevent OCR. The purpose can also be to test the robustness of CAPTCHA anti-bot systems.
        - Assistive technology for blind and visually impaired users
        - Writing the instructions for vehicles by identifying CAD images in a database that are appropriate to the vehicle design as it changes in real time.
        - Making scanned documents searchable by converting them to searchable PDFs
        """)

    with col3:
        st.markdown(
            """
        ## OCR Types

        - Optical character recognition (OCR) – targets typewritten text, one glyph or character at a time.
        - Optical word recognition – targets typewritten text, one word at a time (for languages that use a space as a word divider). (Usually just called "OCR".)
        - Intelligent character recognition (ICR) – also targets handwritten printscript or cursive text one glyph or character at a time, usually involving machine learning.
        - Intelligent word recognition (IWR) – also targets handwritten printscript or cursive text, one word at a time. This is especially useful for languages where glyphs are not separated in cursive script.

        OCR is generally an "offline" process, which analyses a static document. There are cloud based services which provide an online OCR API service. Handwriting movement analysis can be used as input to handwriting recognition.[14] Instead of merely using the shapes of glyphs and words, this technique is able to capture motions, such as the order in which segments are drawn, the direction, and the pattern of putting the pen down and lifting it. This additional information can make the end-to-end process more accurate. This technology is also known as "on-line character recognition", "dynamic character recognition", "real-time character recognition", and "intelligent character recognition".
    """)


st.markdown(
    """"
    source : [Wikipedia](https://en.wikipedia.org/wiki/Optical_character_recognition)    
    """
)
