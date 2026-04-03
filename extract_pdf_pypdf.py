import pypdf
pdf_path = r"c:\Users\ajayc\Downloads\Raghu ram CV.pdf"
reader = pypdf.PdfReader(pdf_path)
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"
with open(r"c:\Users\ajayc\Downloads\raghu portfolio\cv_text.txt", "w", encoding="utf-8") as f:
    f.write(text)
print("Extraction Complete")
