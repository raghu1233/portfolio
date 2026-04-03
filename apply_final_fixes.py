import shutil

src_img = r'C:\Users\ajayc\.gemini\antigravity\brain\7c12764f-b281-4a1a-a386-fb3ea6386b3a\media__1774551911655.jpg'
dst_img = r'C:\Users\ajayc\Downloads\portfolio1\profile.jpg'
shutil.copy(src_img, dst_img)

with open(r'C:\Users\ajayc\Downloads\portfolio1\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<title>Velagapudi Sai Tanmai — Portfolio</title>', '<title>Ajay Chinthakindi — Portfolio</title>')

with open(r'C:\Users\ajayc\Downloads\portfolio1\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
