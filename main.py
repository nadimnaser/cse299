import cv2
import cvzone
import pyautogui
import numpy as py
import streamlit as st
from PIL import Image

cap = cv2.VideoCapture(0)
st.title("CSE299 Project")
start_button_pressed = st.button("Start")
stop_button_pressed = st.button("Stop")
capture_button_pressed = st.button("Capture")
native_filter = st.button("Native Filter")
pirate_filter = st.button("Pirate Filter")
sunglass_filter = st.button("Sunglass Filter")
star_filter = st.button("Star Filter")

filter: str = 'star.png'

if pirate_filter:
    filter: str = 'pirate.png'

elif native_filter:
    filter: str = 'native.png'

elif sunglass_filter:
    filter: str = 'sunglass.png'

elif star_filter:
    filter: str = 'star.png'

cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
overlay = cv2.imread(filter, cv2.IMREAD_UNCHANGED)
frame_placeholder = st.empty()
image = Image.open('savedimg.jpg')
st.image(image, caption='Enter any caption here')

while cap.isOpened() and not stop_button_pressed:
    _, frame = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray_scale)
    for (x, y, w, h) in faces:
        # cv2.rectangle(frame,(x, y), (x+w, y+h), (0, 255, 0), 2)
        overlay_resize = cv2.resize(overlay, (int(w*1.5), int(h*1.5)))
        frame = cvzone.overlayPNG(frame, overlay_resize, [x-55, y-75])
    # cv2.imshow('Snap Dude', frame)
    frame_placeholder.image(frame, channels="RGB")


    if cv2.waitKey(1) == ord('q') or stop_button_pressed:
        break

    if cv2.waitKey(2) == ord('s') or capture_button_pressed:
        cv2.imwrite('savedimg.jpg', frame)
        print("Image is saved")
        cv2.destroyAllWindows()


