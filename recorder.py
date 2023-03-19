import multiprocessing
import ctypes

from process.processControl import startControlProcess
from process.processOCR import startOCRProcess
from process.processUI import startUIProcess

if __name__ == '__main__':

    if_start_ocr = multiprocessing.Manager().Value(ctypes.c_int, 0)
    if_window_open_focus = multiprocessing.Manager().Value(ctypes.c_int, 0)
    mouse_click_pos = multiprocessing.Manager().dict()
    mouse_click_pos['x'] = 0
    mouse_click_pos['y'] = 0

    pControl = multiprocessing.Process(target=startControlProcess, args=(if_start_ocr,if_window_open_focus,mouse_click_pos,))
    pOcr = multiprocessing.Process(target=startOCRProcess, args=(if_start_ocr,if_window_open_focus,mouse_click_pos,))
    pUi = multiprocessing.Process(target=startUIProcess, args=(if_window_open_focus,))
    pControl.start()
    pOcr.start()
    pUi.start()

    pControl.join()
    pOcr.join()
    pUi.join()