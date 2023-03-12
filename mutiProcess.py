from multiprocessing import Process

import time

class mProcess(Process):
    def __init__(self, name):
        super(mProcess, self).__init__()
        self.name = name
 
    def run(self):
        print('process name :' + str(self.name))
        time.sleep(1)