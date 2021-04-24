import cv2
import numpy as np

cap = cv2.VideoCapture('vtest.avi')

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2) # O movimento é a diferença entre dois quadros
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0) # a diferença tem ruídos por causa dos detalhes e da luz no vídeo, então o desfoque gaussiano está eliminando os ruídos
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) # obter o limite da diferença clara
    dilated = cv2.dilate(thresh, None, iterations=3) # dilatae para eliminar as pequenas linhas de limite fraco do distrito que corrompem a detecção de limite saudável
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # encontrar contornos a partir do limite limpo

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        # eliminando pequenos contornos que não podem ser humanos ao filtrar a área de contorno
        if cv2.contourArea(contour) < 700 or (h/w)<=1:
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2) # desenho de retângulos para cada contorno detectado no quadro, dimensões do retângulo obtidas de cv2.boundingRect
        cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    cv2.imshow("feed",frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()
