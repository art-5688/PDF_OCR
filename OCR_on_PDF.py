import os
import pytesseract
from pdf2image import convert_from_path
import cv2
import numpy as np
from PIL import Image


class ScannedPDFExtractor:
    def __init__(self):
        # ✅ Set Tesseract path (change if different)
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

        # ✅ Set Poppler path
        self.poppler_path = r"C:\poppler-25.12.0\Library\bin"

        # 🔥 Force PATH for Windows Store Python issue
        os.environ["PATH"] += os.pathsep + self.poppler_path

        self.dpi = 300

    # -----------------------------
    # PDF → Images
    # -----------------------------
    def pdf_to_images(self, pdf_path):
        try:
            images = convert_from_path(
                pdf_path,
                dpi=self.dpi,
                poppler_path=self.poppler_path
            )
            return images
        except Exception as e:
            raise Exception(f"PDF to image conversion failed: {str(e)}")

    # -----------------------------
    # Preprocessing
    # -----------------------------
    def preprocess_image(self, image):
        try:
            img = np.array(image)

            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Noise removal
            blur = cv2.GaussianBlur(gray, (5, 5), 0)

            # Adaptive threshold (better than fixed)
            thresh = cv2.adaptiveThreshold(
                blur,
                255,
                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                cv2.THRESH_BINARY,
                11,
                2
            )

            return thresh
        except Exception as e:
            raise Exception(f"Image preprocessing failed: {str(e)}")

    # -----------------------------
    # OCR
    # -----------------------------
    def extract_text_from_image(self, image):
        try:
            config = r'--oem 3 --psm 6'
            text = pytesseract.image_to_string(image, config=config)
            return text
        except Exception as e:
            raise Exception(f"OCR failed: {str(e)}")

    # -----------------------------
    # Full Pipeline
    # -----------------------------
    def extract_from_pdf(self, pdf_path):
        try:
            images = self.pdf_to_images(pdf_path)

            results = []

            for i, image in enumerate(images):
                processed = self.preprocess_image(image)
                text = self.extract_text_from_image(processed)

                results.append({
                    "page": i + 1,
                    "text": text
                })

            return results

        except Exception as e:
            raise Exception(f"Extraction pipeline failed: {str(e)}")


# -----------------------------
# MAIN EXECUTION
# -----------------------------
if __name__ == "__main__":
    try:
        extractor = ScannedPDFExtractor()

        pdf_path = "PDF_Doc1.pdf"  # change if needed

        result = extractor.extract_from_pdf(pdf_path)

        for page in result:
            print(f"\n===== PAGE {page['page']} =====\n")
            print(page["text"])

    except Exception as e:
        print("ERROR:", str(e))