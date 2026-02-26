from pypdf import PdfReader, PdfWriter

file = open('pdflatex-image.pdf','rb')
pdf_reader = PdfReader(file)
# print(pdf_reader.get_num_pages())
page_one = pdf_reader.get_page(0)
# page_one_text = page_one.extract_text()
# print(page_one_text)
# file.close()

pdf_writer = PdfWriter()
pdf_writer.add_page(page_one)

pdf_output = open('some_brandnew_doc.pdf', 'wb')
pdf_writer.write(pdf_output)

file.close()
pdf_output.close()
