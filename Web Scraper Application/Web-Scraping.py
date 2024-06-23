import streamlit as st
import requests
from bs4 import BeautifulSoup
import PyPDF2
from io import BytesIO
import zipfile
import os
from urllib.parse import urlparse

MAX_ZIP_FILE_SIZE = 1024 * 1024 * 100  # 100 MB
MAX_ZIP_FILE_COUNT = 50

st.title("Web Scraper")
st.subheader("Streamlit Web Scraper for all Web Scraping Functionalities")
st.text("Enter Your Website Link and Get all Web Scraping Functions for it.")

try:
    link = st.text_input("Enter Website Link")
    parsed_url = urlparse(link)
    domain_name = parsed_url.netloc.split('.')[0] if parsed_url.netloc.split('.')[0] != 'www' else parsed_url.netloc.split('.')[1]
    st.write("Domain Name:", domain_name.capitalize())
except:
    st.write("Please Give Valid URL")

def establish_Connection(link):
    try:
        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'lxml')
        return soup
    except:
        st.write(f"Connection to {link} cannot be established. Try with another Website")

def save_to_file(data, fname):
    if data:
        st.download_button(
            label="Download Text File",
            data='\n'.join(data),
            file_name=fname,
            key="download_button",
        )
    else:
        st.write("No data to download.")

def button_Print(data, statement):
    if data:
        if st.button(statement):
            st.write(data)

def link_Check(link):
    if link.endswith(('pdf', 'jpeg', 'jpg', 'png', 'svg', 'webp')):
        st.write(f"This is a {link.split('.')[-1].upper()} File.")
        return link.split('.')[-1]
    else:
        return "normal"

def embedded_links(link):
    try:
        if link_Check(link) == "normal":
            soup = establish_Connection(link)
            links = soup.find_all('a')
            if links:
                embed_link = [link.get('href') for link in links if link.get('href') and not link.get('href').startswith("#")]
                if embed_link:
                    fname = f"{domain_name.capitalize()}_Embedded_links_Website.txt"
                    save_to_file(embed_link, fname)
                    button_Print(embed_link, "See Embedded Links")
                else:
                    st.write("Website Has No Embedded Links!!")
            else:
                st.write("Website Has No Embedded Links!!")
    except:
        st.write("Website Has No Embedded Links!!")

visited_links = []

def main_website_text_Data(link):
    global visited_links
    try:
        if link_Check(link) == "normal" and link not in visited_links:
            soup = establish_Connection(link)
            text = soup.get_text()
            if text:
                fname = f"{domain_name.capitalize()}_Main_Website_Data.txt"
                save_to_file(text, fname)
                button_Print(text, "See Scraped Data")
            else:
                st.write("Website Has No Data!!")
            visited_links.append(link)
    except:
        visited_links.append(link)
        st.write("Website does not have any Text Data!!")

# Define other functions similarly...

if __name__ == "__main__":
    utility = st.selectbox("Utility:", ['Embedded Links', 'Main Website Text Data', 'Complete Website Text Data', 
                                        'Main Website Text Data along with Embedded Links Text Data', 'Extract Text from PDF Link',
                                        'Main Website PDF Data along with Embedded Links PDF Data', 'Complete Website PDF Data', 
                                        'Complete Website Text and PDF Data', 'Download PDF Files From Main Website', 
                                        'Download All PDF Files From Website', 'Download Image Files From Main Website', 
                                        'Download All Image Files From Website'])
    
    if utility == 'Embedded Links':
        embedded_links(link)
    elif utility == 'Main Website Text Data':
        main_website_text_Data(link)
    # Add other utility functions here...
    
    try:
        if st.button("Close App"):
            st.experimental_clear_cache()
            st.stop()
    except:
        pass
