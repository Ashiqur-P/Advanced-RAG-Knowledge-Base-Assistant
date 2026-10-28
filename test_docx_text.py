from docx import Document
from pathlib import Path

file_path = Path(r"C:\Users\ASUS\Downloads\বাংলাদেশ ও বিশ্ব পরিচয় এবং বিজ্ঞান .docx")

doc = Document(file_path)

for paragraph in doc.paragraphs:
    text = paragraph.text.strip()
    if text:
        print(text)
