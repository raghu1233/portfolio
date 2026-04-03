import sys
import os

try:
    import PyPDF2
except ImportError:
    os.system(sys.executable + " -m pip install PyPDF2")
    import PyPDF2

pdf_path = r"c:\Users\ajayc\Downloads\Raghu ram CV.pdf"
text = ""

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
    
    with open(r"c:\Users\ajayc\Downloads\raghu portfolio\cv_text.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("Extraction Complete")
except Exception as e:
    print(f"Error during extraction: {e}")
