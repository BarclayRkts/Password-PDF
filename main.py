import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path


def getFile(password):

    # The location of the PDF files you want to add a password to. Ex: E:\Documents\FilesToAddPasswordto
    file_location = '----------Fill----------' 
    
    # goes through all files in directory (file_location).
    for root, subdirs, files in os.walk(file_location): 

        for file in files:
            if(Path(file).suffix == '.pdf'):
                print("file: " + file)
                print("root: " + root)
                print("subdirs: " + str(subdirs))
                Encrypt(password, file, file_location, root)


def Encrypt(password, file, file_location, root):
    print(root)
    pdfFile = open(root + "\\" + file, 'rb')

    # Create reader and writer object
    input_pdf = PdfFileReader(pdfFile)
    pdfWriter = PdfFileWriter()

    # Add all pages to writer (accepted answer results into blank pages)
    for pageNum in range(input_pdf.numPages):
        pdfWriter.addPage(input_pdf.getPage(pageNum))
    
    # Encrypt with your password
    pdfWriter.encrypt(password)

    file_name = os.path.splitext(str(file))

    # The location you want to store the PDF files Ex: E:\Documents\NewFiles
    resultPdf = open('----------Fill----------' + file_name[0] + '_encrypted' + file_name[1], 'wb')
    pdfWriter.write(resultPdf)
    print(resultPdf)
    resultPdf.close()



password = input("Give the pdfs a password: ")
getFile(password)

