import pytesseract
from PIL import Image
import cv2
import os

IMAGE_FOLDER = "images"

for img_file in os.listdir(IMAGE_FOLDER):
    if img_file.lower().endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(IMAGE_FOLDER, img_file)
        img = cv2.imread(img_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        text = pytesseract.image_to_string(thresh)
        print(f"\n--- Text from {img_file} ---")
        print(text)