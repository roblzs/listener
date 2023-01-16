import speech_recognition as sr
 
# initialize the recognizer
r = sr.Recognizer()
 
# Capture audio from microphone
with sr.Microphone() as source:
    print("Talk: ")
    audio = r.listen(source)
 
try:
    # Prints the output of the audio file in text format
    text = r.recognize_google(audio)
    print("You said:", text)

    # Writing the output to a text file
    with open("output.txt", "w") as f:
        f.write(text)
        
except:
    print("Sorry, I dumb robot")
