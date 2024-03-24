import paddleocr
import cv2
import numpy as np
import pandas as pd

# Initialize OCR reader
ocr = paddleocr.PaddleOCR(use_angle_cls=True)

# Read image
img_path = 'C:/Users/Sharda Prasad Maurya.LAPTOP-4MVRVONI/Desktop/assignment/Image/image00013.jpg'

img = cv2.imread(img_path)

# Perform OCR
result = ocr.ocr(img)

# Extract table from OCR result
table_texts = []
for line in result:
    text = line[1][0]
    if '|' in text:  # Assuming '|' indicates table cell separation
        table_texts.append(text)

# Convert table data to DataFrame
table_data = [row.split('|') for row in table_texts]
df = pd.DataFrame(table_data)

# Save DataFrame to Excel file
excel_file_path = 'output_table.xlsx'
df.to_excel(excel_file_path, index=False)

print("Table extracted and saved as:", excel_file_path)
