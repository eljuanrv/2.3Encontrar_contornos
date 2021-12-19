import cv2
import numpy as np

cap = cv2.VideoCapture(0)

verdeClaro = np.array([60,0,0],np.uint8)
verdeOscuro = np.array([120,255,255],np.uint8)

while(True):
    ret,frame = cap.read()
    if (ret ==  True):
        frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(frameHSV,verdeClaro,verdeOscuro)
        contornos,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        #retr_external: solo se queda con los contornos externos
        #chain approx simple encierra al contorno en cuantro puntos
        #variable contornos es vectorial
        for c in contornos:
        	area =  cv2.contourArea(c)
        	if area > 4000:              #contourldx (0,-1), color, line tipe
        		cv2.drawContours(frame,[c],0, (255,0,0), 3)
        cv2.imshow('Contours', mask)
        cv2.imshow('Frame', frame)
        if(cv2.waitKey(1) & 0xFF==ord('s')):
        	break
cv2.waitKey(0)
cv2.destroyAllWindows()