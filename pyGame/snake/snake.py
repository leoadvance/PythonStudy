# couding=utf-8
import re
import time

class snake():

    def __init__(self, name: str):
        print("class %s init!" %name)
        self.name = name

    def __del__(self):
        print("class %s delete!" %self.name)



    def run(self):

        startTime = time.time()

        endTime = time.time()
        print("%s run time: "%self.name, (str(endTime - startTime))[:8], "s")

        pass

