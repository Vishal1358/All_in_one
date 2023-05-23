import PyPDF2

f = open("Working_Business_Proposal.pdf","rb")
pdf_reader =PyPDF2.PdfFileReader(f)
pdf_reader.numPages