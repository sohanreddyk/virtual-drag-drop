import cv2
from cvzone.HandTrackingModule import HandDetector

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set width
cap.set(4, 720)   # Set height

# Initialize hand detector
detector = HandDetector(detectionCon=0.8)

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture webcam feed. Exiting...")
        break
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    # Display the webcam feed
    cv2.imshow("Webcam Feed", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()