# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 15:33:05 2022

@author: User
"""
import cv2
import numpy as np
import HandTrackingModule as htm
import time
import math

cap = cv2.VideoCapture(0)
detector = htm.handDetector(detectionCon=0.7)

pTime = 0

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw=False)
    if len(lmlist) > 0:
        # print(lmlist[4], lmlist[8])

        x1, y1 = lmlist[4][1], lmlist[4][2]
        x2, y2 = lmlist[8][1], lmlist[8][2]
        x3, y3 = lmlist[12][1], lmlist[12][2]
        x4, y4 = lmlist[16][1], lmlist[16][2]
        x5, y5 = lmlist[20][1], lmlist[20][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        cv2.circle(img, (x1, y1), 5, (0, 215, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 5, (0, 215, 255), cv2.FILLED)
        cv2.circle(img, (cx, cy), 5, (0, 215, 255), cv2.FILLED)
        cv2.circle(img, (x3, y3), 5, (0, 215, 255), cv2.FILLED)
        cv2.circle(img, (x4, y4), 5, (0, 215, 255), cv2.FILLED)
        cv2.circle(img, (x5, y5), 5, (0, 215, 255), cv2.FILLED)

        cv2.line(img, (x1, y1), (x2, y2), (0, 215, 255), 3)
        cv2.line(img, (x2, y2), (x3, y3), (0, 215, 255), 3)
        cv2.line(img, (x3, y3), (x4, y4), (0, 215, 255), 3)
        cv2.line(img, (x4, y4), (x5, y5), (0, 215, 255), 3)
        length = math.hypot(x2 - x1, y2 - y2)
        print(length)
        if length < 35:
            cv2.circle(img, (cx, cy), 15, (255, 0, 0), cv2.FILLED)
        if length > 200:
            cv2.circle(img, (cx, cy), 15, (255, 127, 80), cv2.FILLED)
        # range 35-200
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'GAYMETER:{int(fps)}', (20, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)
    cv2.imshow("Img", img)

    cv2.waitKey(1)
