# OCR Text Extraction

This is a simple project for extracting text from images using **Tesseract OCR** with basic preprocessing (OpenCV).

## 📌 Purpose

I built this to understand how OCR works so I can later integrate text extraction into a **document classification model**.

## ▶️ How to Run

### 1. Clone the repo

```
git clone https://github.com/YOUR_USERNAME/ocr-text-extraction.git
cd ocr-text-extraction
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Install Tesseract

* Linux:

```
sudo apt install tesseract-ocr
```

### 4. Add images

Put your images inside the `images/` folder.

### 5. Run

```
python ocr_test.py
```

---

## 🐳 Docker (optional)

```
docker build -t ocr-app .
docker run --rm -v ${PWD}/images:/app/images ocr-app
```
