from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2
import asyncio
from multiprocessing import Process, Queue
 
ap = argparse.ArgumentParser()

ap.add_argument("-o", "--output", type=str, default="barcodes.csv",

            help="path to output CSV file containing barcodes")

args = vars(ap.parse_args())

vs = VideoStream(src=0).start()
 
def camera():
    

    time.sleep(2.0)

    while True:

        frame = vs.read()

        frame = imutils.resize(frame, width=1200)

        barcodes = pyzbar.decode(frame)
        
        
        for barcode in barcodes:
            barcodeData = barcode.data.decode("utf-8")
            barcodeType = barcode.type
            if barcodeData:
                return barcodeData
        if not barcodes:
            pass
        key = cv2.waitKey(1) & 0xFF
        # if the `s` key is pressed, break from the loop
        if key == ord("s"):
            break
#print("[INFO] cleaning up...")
#cv2.destroyAllWindows()
#vs.stop()
    

