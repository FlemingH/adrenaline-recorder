import multiprocessing
import ctypes

from process.processControl import startControlProcess
from process.processOCR import startOCRProcess

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

    if_start_ocr = multiprocessing.Manager().Value(ctypes.c_int, 0)
    pControl = multiprocessing.Process(target=startControlProcess, args=(if_start_ocr,))
    pOcr = multiprocessing.Process(target=startOCRProcess, args=(if_start_ocr,))
    pControl.start()
    pOcr.start()

    pControl.join()
    pOcr.join()
    # process = mProcess("OCR")
    # process.start()
    # process = mProcess("UIListener")
    # process.start()
    # process = mProcess("Control")
    # process.start()

    # process.join()