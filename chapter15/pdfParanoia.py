import PyPDF2, os, sys

#Function to encrypt a pdf file
def encrypt():
    for subdir, dirs, files in os.walk('.'):
        for file in files:
            filepath = subdir + os.sep + file
            if file.endswith('.pdf'):
                pdfFile = open(filepath, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFile)
                if pdfReader.isEncrypted==False:
                    pdfWriter = PyPDF2.PdfFileWriter()
                    for pageNum in range(pdfReader.numPages):
                        pdfWriter.addPage(pdfReader.getPage(pageNum))
                    
                    pdfWriter.encrypt(password)
                    resultPdf = open(f'{file[:-4]}_encrypted.pdf', 'wb')
                    pdfWriter.write(resultPdf)
                    resultPdf.close()
def decrypt():
    for subdir, dirs, files in os.walk('.'):
        for file in files:
            filepath = subdir + os.sep + file
            if file.endswith('.pdf'):
                pdfFile = open(filepath, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFile)
                if pdfReader.isEncrypted==True:
                    if pdfReader.decrypt(password)==1:
                        pdfReader.decrypt(password)
                        pdfWriter = PyPDF2.PdfFileWriter()
                        for pageNum in range(pdfReader.numPages):
                            pdfWriter.addPage(pdfReader.getPage(pageNum))
                        
                        resultPdf = open(f'{file[:-4]}_decrypted.pdf', 'wb')
                        pdfWriter.write(resultPdf)
                        resultPdf.close()
                    else:
                        print('Wrong Password')

password = sys.argv[2]
if sys.argv[1]=='encrypt':
    encrypt()
elif sys.argv[1]=='decrypt':
    decrypt()
else:
    print('Invalid input. Enter either encrypt or decrypt.')
