"""This is where we parse the PDF"""
from fastapi import UploadFile
from pdf2image import convert_from_bytes
import pytesseract

def parse_pdf(file: UploadFile):

    file.file.seek(0) # Move the file pointer back to 0 to read from the PDF again 
    pdf_bytes = file.file.read()
    images = convert_from_bytes(pdf_bytes)

    # Turn them into text
    text = ""
    for i, image in enumerate(images):
        print(f"-----PAGE {i + 1} ------- ")
        page_text = pytesseract.image_to_string(image)
        print(page_text) # Let's see the current text currently
        text += page_text
    
    return text 


def chunk_text(text: str): 

    # Then we perform chunking 
    pass # To be implemented later 

