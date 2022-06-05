import cv2
import mediapipe as mp
from math import hypot


cap = cv2.VideoCapture(0)
cap.set(3, 360)
cap.set(4, 240)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


def check():
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    lmList = []
    if results.multi_hand_landmarks:
        for handlandmark in results.multi_hand_landmarks:
            for id, lm in enumerate(handlandmark.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id, cx, cy])
            mpDraw.draw_landmarks(img, handlandmark, mpHands.HAND_CONNECTIONS)

    if lmList != []:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        x3, y3 = lmList[12][1], lmList[12][2]
        x4, y4 = lmList[16][1], lmList[16][2]
        x5, y5 = lmList[20][1], lmList[20][2]

        length54 = hypot(x5-x4, y5-y4)
        length43 = hypot(x4-x3, y4-y3)
        length32 = hypot(x3-x2, y3-y2)
        length21 = hypot(x2-x1, y2-y1)

        if length21 < 50 and length32 < 50 and length43 < 50 and length54 < 50:
            return True

    cv2.imshow('Dinnnnnno!', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        exit()
