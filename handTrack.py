import cv2
from cvzone import HandTrackingModule

cap = cv2.VideoCapture(0)
detector = HandTrackingModule.HandDetector()

while (True):
    success, img = cap.read()
    detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)

    if lmList:
        # Check for gestures
        # Example: Check for thumbs up gesture
        if lmList[4][1] < lmList[3][1]:  # Thumb tip above index finger tip
            cv2.putText(img, "Thumbs Up", (lmList[4][1], lmList[4][2]), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        # Add more gesture checks here

    cv2.imshow("Image", img)
    cv2.waitKey(1)
