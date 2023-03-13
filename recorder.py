from mutiProcess import mProcess
from multiprocessing import Value

# start two process to doing the OCR while listen the UI change
# p = mProcess("OCR")
# p.start()
# p = mProcess("UIListener")
# p.start()
# p = mProcess("ControlProcess")
# p.start()

# p.join()
# p.join()
# p.join()
# processControl.join()

if __name__ == '__main__':

    # process = mProcess("OCR")
    # process.start()
    # process = mProcess("UIListener")
    # process.start()
    process = mProcess("Control")
    process.start()

    process.join()