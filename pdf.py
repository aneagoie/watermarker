# OLD: import PyPDF2
# NEW: 
import pypdf

# template = PyPDF2.PdfFileReader(open('superduper.pdf', 'rb'))
# watermark = PyPDF2.PdfFileReader(open('water.pdf', 'rb'))
# output = PyPDF2.PdfFileWriter()

# THIS IS THE NEW WAY TO DO THIS:
template = pypdf.PdfReader(open('superduper.pdf', 'rb'))
watermark = pypdf.PdfReader(open('water.pdf', 'rb'))
output = pypdf.PdfWriter()


# for i in range(template.getNumPages()):
# THIS IS THE NEW WAY TO DO THIS:
for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)
 
with open('watermaked_output.pdf', 'wb') as outputFile:
    output.write(outputFile)
    

 


 
 

 


 
