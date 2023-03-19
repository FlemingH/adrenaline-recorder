# Internal OCR Tools
import CNOCR
ocr = CNOCR.getCNOCRObj()
from uiControl import FormControl
import os
from datetime import datetime

def writeOCRLog(text):

    if not os.path.exists("log"):
        os.mkdir(r"log")

    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day

    with open(rf"log\{year}-{month}-{day}-OCR.txt", "a", encoding="utf-8") as f:
        print("write text: "+text)
        f.write(text)

def startOCRProcess(if_start_ocr, if_window_open_focus, mouse_click_pos):
    
    startNewLine = 0
    while True:
        # app start set new line
        if if_window_open_focus.value == 1:
            if startNewLine == 0:
                writeOCRLog("\napp opened, ")
                startNewLine = 1
        else: 
            startNewLine = 0

        if if_start_ocr.value == 1:

            if_start_ocr.value = 0
            x_click = mouse_click_pos['x']
            y_click = mouse_click_pos['y']

            formControl = FormControl()
            monitor_width, monitor_height = formControl.getDeviceCaps()

            #   ----------------
            #   |      | h     |
            #   |      |       |
            #   |------.-------       
            #   |      |   w   |
            #   |      |       |
            #   ----------------
            #
            #   w=0.0129, h=0.0185
            #   ocr in the box
            bbox = (
                x_click/monitor_width-0.0129,
                y_click/monitor_height-0.0185,
                x_click/monitor_width+0.0129,
                y_click/monitor_height+0.0185
            )

            ocr_data, _ = ocr.get_ocr_data_by_bbox(bbox=bbox, save_res=True)
            for data in ocr_data:
                writeOCRLog(str(data.get_data()[5])+", ")