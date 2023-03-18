# Internal OCR Tools
import CNOCR
ocr = CNOCR.getCNOCRObj()
from uiControl import FormControl

def startOCRProcess(if_start_ocr):
    while True:
        if if_start_ocr.value == 1:
            print("start ocr")
            if_start_ocr.value = 0
