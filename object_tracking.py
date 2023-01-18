#lendo video e mandando aparecer na tela

import cv2
import time
import math

video = cv2.VideoCapture("bb3.mp4")

while True:
    
    check, img = video.read()   

    # Exiba o vídeo
    cv2.imshow("resultado", img)


    # Saia da janela de exibição quando a barra de espaço for pressionada
    key = cv2.waitKey(25)
    if key == 32:
        print("Interrompido")
        break

video.release()
cv2.destroyALLwindows()
