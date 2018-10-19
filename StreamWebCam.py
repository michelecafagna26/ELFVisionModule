import cv2
import sys
import API_Class

def demo(myAPI):
    myAPI.initializer()
    video_capture = cv2.VideoCapture(0)
    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read() #np.array

        frame = myAPI.caller(frame)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()


demo(API_Class.openCV())
# demo(API_Class.SkyBiometry())
# demo(API_Class.Azure(API_Class.Azure.url_face, API_Class.Azure.key_face, API_Class.Azure.params_face))