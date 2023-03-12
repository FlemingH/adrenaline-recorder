from mutiProcess import mProcess

# start two process to doing the OCR while listen the UI change
processOCR = mProcess("OCR")
processUIListener = mProcess("UIListener")
processOCR.start()
processUIListener.start()