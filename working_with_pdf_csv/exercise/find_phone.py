from pypdf import PdfReader, PdfWriter
import re

file = open('Find_the_Phone_Number.pdf','rb')
pdf_reader = PdfReader(file)

len_pdf_page = len(pdf_reader.pages)

for i in range(len_pdf_page):
    page = pdf_reader.get_page(i)
    text_on_page = page.extract_text()
    # 505.503.4455
    pattern = r'\d{3}.\d{3}.\d{4}'
    is_number = re.search(pattern, text_on_page)
    if is_number:
        print(is_number.group().replace('.', ' '))
