import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 360)
cap.set(4, 240)
detector = HandDetector(maxHands=1, detectionCon=0.8)

def check():
    _, img = cap.read()
    img = cv2.flip(img, 1)
    hand = detector.findHands(img, draw=False)
    if hand:
        lmlist = hand[0]
        if lmlist:
            fingerup = detector.fingersUp(lmlist)
            if fingerup == [1, 1, 1, 1, 1]:
                return True

    cv2.imshow('Dinnnnnno!', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        exit()
