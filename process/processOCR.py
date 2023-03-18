# Internal OCR Tools
import CNOCR
ocr = CNOCR.getCNOCRObj()
from uiControl import FormControl

def startOCRProcess(if_start_ocr, mouse_click_pos):
    while True:
        if if_start_ocr.value == 1:
            print("start ocr", mouse_click_pos['x'], mouse_click_pos['y'])
            if_start_ocr.value = 0
