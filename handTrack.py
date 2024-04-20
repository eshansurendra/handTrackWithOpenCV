import cv2
from cvzone import HandTrackingModule

cap = cv2.VideoCapture(0)
detector = HandTrackingModule.HandDetector()

while True:
    success, img = cap.read()
    detector.findHands(img)
    lmList, _ = detector.findPosition(img)

    if lmList:
        # Gesture recognition: Thumbs up
        if lmList[4][1] < lmList[3][1] and lmList[8][2] < lmList[6][2]:  # Thumb tip above index finger tip and thumb tip below wrist
            cv2.putText(img, "Thumbs Up", (lmList[4][1], lmList[4][2]), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        # Gesture recognition: Peace sign
        if lmList[6][2] < lmList[8][2] and lmList[10][2] < lmList[8][2]:  # Index and middle finger tips above thumb tip
            cv2.putText(img, "Peace Sign", (lmList[8][1], lmList[8][2]), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        # Gesture recognition: OK sign
        if lmList[4][1] < lmList[3][1] and lmList[8][1] < lmList[7][1]:  # Thumb tip above index finger tip and index finger tip to the left of thumb tip
            cv2.putText(img, "OK Sign", (lmList[8][1], lmList[8][2]), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
