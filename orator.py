import pyttsx3
import PyPDF2
import os
import sys

file = sys.argv[1]

if os.path.exists(file):
    print("Now reading " + os.path.basename(file))
    # file exists
    pdfreader = PyPDF2.PdfFileReader(open(file,'rb'))
    speaker = pyttsx3.init()
else:
    print("Error - File or path does not exist")


print("\033[1;36;40m Ahem...(∩｀-´)⊃━☆ﾟ.*･｡ﾟ \n")

for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText()  ## extracting text from the PDF
    cleaned_text = text.strip().replace('\n',' ')  ## Removes unnecessary spaces and break lines
    print(cleaned_text)                ## Print the text from PDF
    speaker.say(cleaned_text)        ## Let The Speaker Speak The Text
    #speaker.save_to_file(cleaned_text,'story.mp3')  ## Saving Text In a audio file 'story.mp3'
    speaker.runAndWait()
speaker.stop()
