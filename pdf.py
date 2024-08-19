import PyPDF2

# template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
# watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
# output = PyPDF2.PdfFileWriter()
# This is the new way to do this:
template = PyPDF2.PdfReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfWriter()


# for i in range(template.getNumPages()):
# New way to do this:
for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)
 
with open('watermaked_output.pdf', 'wb') as outputFile:
    output.write(outputFile)
    

 


 
 

 


 
