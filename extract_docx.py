import zipfile
import xml.etree.ElementTree as ET

def get_docx_text(path):
    try:
        document = zipfile.ZipFile(path)
        xml_content = document.read('word/document.xml')
        document.close()
        tree = ET.XML(xml_content)

        paragraphs = []
        for paragraph in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
            texts = [node.text
                     for node in paragraph.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
                     if node.text]
            if texts:
                paragraphs.append(''.join(texts))

        return '\n'.join(paragraphs)
    except Exception as e:
        return str(e)

text = get_docx_text(r'c:\Users\ajayc\Downloads\portfolio1\AJ.updated.CV.docx')
with open(r'c:\Users\ajayc\Downloads\portfolio1\AJ.updated.CV.txt', 'w', encoding='utf-8') as f:
    f.write(text)
