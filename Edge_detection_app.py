# Importing Libraries
import cv2

# Defining the video capture device
cap = cv2.VideoCapture(0)

# Creating a loop so that the application works in real time
while cap.isOpened():
    ret, frame = cap.read()

    # using canny to identify the edges
    canny = cv2.Canny(frame, threshold1=180, threshold2=200)

    cv2.imshow('Webcam', canny)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
