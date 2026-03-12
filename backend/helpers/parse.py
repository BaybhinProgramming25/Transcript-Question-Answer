"""This is where we parse the PDF"""
from helpers.classcontent import get_content_from_each_sem
from helpers.semmapping import get_sem_mapping

import fitz 

def parse_pdf(file_bytes) -> list[str]:

    doc = fitz.open(stream=file_bytes, filetype="pdf")

    pdf_pages_list = []
    for page in doc:
        text = page.get_text("text").strip("").split("\n")
        pdf_pages_list.extend(text)

    sm_ll = get_sem_mapping(pdf_pages_list)
    student_classes = get_content_from_each_sem(sm_ll, pdf_pages_list) 
    return student_classes[0] # Just return the first item for now 


def chunk_pdf(text_list: list) -> list[str]:

    chunk_size = 5
    chunk_overlap = 2

    chunks = []
    start = 0

    while start < len(text_list):
        end = start + chunk_size
        chunk_words = text_list[start:end]
        chunk_text = " ".join(chunk_words)

        chunks.append(chunk_text)
        start += chunk_size - chunk_overlap
    return chunks 
