import speech_recognition as sr
 
r = sr.Recognizer()
 
with sr.Microphone() as source:
    print("Talk: ")
    audio = r.listen(source)
 
try:
    text = r.recognize_google(audio)
    print("You said:", text)

    with open("output.txt", "w") as f:
        f.write(text)
        
except:
    print("Sorry, I dumb robot")
