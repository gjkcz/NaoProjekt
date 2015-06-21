class MyClass(GeneratedClass):
    def __init__(self):
        try: # disable autoBind
            GeneratedClass.__init__(self, False)
        except TypeError: # if NAOqi < 1.14
            GeneratedClass.__init__( self )

        self.tts = ALProxy("ALTextToSpeech")
        self.sentences = {
            "English" : " Hello, my name is Naome. Nela taught me how to dance. Let me show you! ",
            "Czech" : " Nela mě naučila tančit. Koukej! "
        }

    def onInput_onStart(self):
        sDefaultLang = self.tts.getLanguage()
        self.onStopped(self.sentences[sDefaultLang])
