import speech_recognition as sr

class SpeechRecognition(object):
    """Speech through input"""
    def __init__(self):
        self.RecentCommandAudio = None
        self.r = sr.Recognizer()

    # obtain audio from the microphone    
    def CommandCapture(self):
        with sr.Microphone() as source:
            print("Say something!")
            self.RecentCommandAudio = self.r.listen(source)
    def ReadBackLastCommand(self):
        if self.RecentCommandAudio != None:        
            try:
                print(self.r.recognize_sphinx(self.RecentCommandAudio))
            except sr.UnknownValueError:
                print("Sphinx could not understand audio")
            except sr.RequestError as e:
                print("Sphinx error; {0}".format(e)) 
        else:
            print("No Command Was Said")
    def GetCommandToString(self):
        if self.RecentCommandAudio != None:
            return self.r.recognize_sphinx(self.RecentCommandAudio)
        else:
            return False

while True:
    Sp = SpeechRecognition()
    Sp.CommandCapture()
    Sp.ReadBackLastCommand()


