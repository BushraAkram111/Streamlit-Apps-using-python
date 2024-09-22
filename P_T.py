import streamlit as st
from PIL import Image
import pytesseract

# Title of the app
st.title("Picture to Text Converter")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Open the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    # Perform OCR on the image
    st.write("Extracting text...")
    text = pytesseract.image_to_string(image)
    
    # Display the extracted text
    st.text_area("Extracted Text", text, height=250)

# Footer
st.write("Developed by Bushra Akram")
