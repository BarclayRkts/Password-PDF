import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PyPDF2 import PdfFileReader, PdfFileWriter
import shutil
from pathlib import Path
import time

#E:\Documents\FilestoEncrypt
# E:\Documents\TestFile

def getFile(password):
    file_location = 'E:\Documents\FilestoEncrypt'

    for root, subdirs, files in os.walk(file_location):

        for file in files:
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

    # Write it to an output file. (you can delete unencrypted version now)
    file_name = os.path.splitext(str(file))
    resultPdf = open('E:\\Documents\EncryptFiles\\' + file_name[0] + '_encrypted' + file_name[1], 'wb')
    pdfWriter.write(resultPdf)
    print(resultPdf)
    resultPdf.close()



password = input("Give the pdfs a password: ")
# password = "Hello"
getFile(password)

