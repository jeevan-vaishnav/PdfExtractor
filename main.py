# pip install pypdf2
import PyPDF2
a = PyPDF2.PdfFileReader('resume.pdf')
# print(a.documentInfo)
# print(a.getNumPages())
# print(a.getPageMode())

str = ""

for i in range(1, 2):
    str += a.getPage(i).extractText()

with open("text.txt", "w", encoding='utf-8') as f:
    f.write(str)
