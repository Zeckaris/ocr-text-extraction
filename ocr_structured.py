import pytesseract
import cv2
import os

IMAGE_FOLDER = "images"
PLAIN_OUTPUT_FOLDER = "plain_output"
STRUCTURED_OUTPUT_FOLDER = "structured_output"

os.makedirs(PLAIN_OUTPUT_FOLDER, exist_ok=True)
os.makedirs(STRUCTURED_OUTPUT_FOLDER, exist_ok=True)

for img_file in os.listdir(IMAGE_FOLDER):
    if img_file.lower().endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(IMAGE_FOLDER, img_file)

        img = cv2.imread(img_path)
        if img is None:
            print(f"Skipping {img_file}, unable to read.")
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(
            blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

        plain_text = pytesseract.image_to_string(thresh)

        base_name = os.path.splitext(img_file)[0]
        plain_file = os.path.join(
            PLAIN_OUTPUT_FOLDER, f"{base_name}_plain.txt"
        )

        with open(plain_file, "w", encoding="utf-8") as f:
            f.write(plain_text)

        print(f"Plain text saved to {plain_file}")


        data = pytesseract.image_to_data(
            thresh, output_type=pytesseract.Output.DICT
        )

        structured_file = os.path.join(
            STRUCTURED_OUTPUT_FOLDER, f"{base_name}_structured.txt"
        )

        with open(structured_file, "w", encoding="utf-8") as f:
            current_line = ""
            prev_line_id = None

            for i in range(len(data['text'])):
                word = data['text'][i].strip()

                if not word:
                    continue

                line_id = (
                    data['block_num'][i],
                    data['par_num'][i],
                    data['line_num'][i]
                )

                if prev_line_id is None:
                    prev_line_id = line_id

                if line_id != prev_line_id:
                    f.write(current_line.strip() + "\n")
                    current_line = ""
                    prev_line_id = line_id

                current_line += word + " "

            if current_line:
                f.write(current_line.strip() + "\n")

        print(f"Structured text saved to {structured_file}")