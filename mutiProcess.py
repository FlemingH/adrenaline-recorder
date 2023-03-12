from multiprocessing import Process
from process.processControl import startControlProcess

import time

class mProcess(Process):
    def __init__(self, name):
        super(mProcess, self).__init__()
        self.name = name
 
    def run(self):
        if (self.name == "Control"):
            # start the pynput's Listener
            startControlProcess()
        if (self.name == "OCR"):
            print("OCR")
            time.sleep(20)
        if (self.name == "UIListener"):
            print("UIListener")
            time.sleep(20)