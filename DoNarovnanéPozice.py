class MyClass(GeneratedClass):
    def __init__(self):
        try: # disable autoBind
          GeneratedClass.__init__(self, False)
        except TypeError: # if NAOqi < 1.14
          GeneratedClass.__init__( self )

    def onLoad(self):
        self.postureProxy = None
        try:
            self.postureProxy = ALProxy("ALRobotPosture")
        except:
            self.logger.error("Module 'ALRobotPosture' not found.")

    def onUnload(self):
        if(self.postureProxy != None):
            self.postureProxy.stopMove()

    def onInput_onStart(self):
        if(self.postureProxy != None):
            result = self.postureProxy.goToPosture("StandInit", 0.8)
            if(result):
                self.success()
            else:
                self.logger.error("Posture StandInit is not a part of the standard posture library or robot cannot reach the posture")
                self.failure()
        else:
            self.failure()

    def onInput_onStop(self):
        self.onUnload()
