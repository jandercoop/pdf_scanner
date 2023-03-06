import pypdf
from pypdf import PdfFileReader

#Define the specific words to search for
searchWords = ['word1', 'word2', 'word3']

#Prompt User to enter the file name
fileName = input('Enter the file name: ')

#If User presses escape, exit the program
if fileName == '\x1b':
    sys.exit()
    
#Open the file
pdfFile = PdfFileReader(open(fileName, 'rb'))

#Get the number of pages in the PDF Document
numPages = pdfFile.getNumPages()

#Loop through the pages in the PDF Document
for i in range(0, numPages):
    #Get the text content of the current page
    pageObj = pdfFile.getPage(i)
    pageText = pageObj.extractText()

    #Search for occurrences of the specific words in the page text
    for word in searchWords:
        if word in pageText:
            print('The word ' + word + ' was found on page ' + str(i))
        
        else:
            print('The word ' + word + ' was not found on page ' + str(i))

#Close the PDF file
pdfFile.close()
