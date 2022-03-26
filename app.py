import PyPDF2
import pyttsx3
  
path = open('Lec 1, Introduction to Effective Writing.pdf', 'rb')
  
pdfReader = PyPDF2.PdfFileReader(path)
  
from_page = pdfReader.getPage(5)
  

text = from_page.extractText()
  
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
