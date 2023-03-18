# Internal OCR Tools
import CNOCR
ocr = CNOCR.getCNOCRObj()
from uiControl import FormControl
import time

def startOCRProcess(if_start_ocr, mouse_click_pos):
    while True:
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
            print(ocr_data)