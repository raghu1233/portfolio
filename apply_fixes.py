import shutil
import re

# Copy the image to the portfolio folder
src_img = r'C:\Users\ajayc\.gemini\antigravity\brain\7c12764f-b281-4a1a-a386-fb3ea6386b3a\media__1774551461846.jpg'
dst_img = r'C:\Users\ajayc\Downloads\portfolio1\profile.jpg'
shutil.copy(src_img, dst_img)

# Update the HTML
with open(r'C:\Users\ajayc\Downloads\portfolio1\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace profile picture
html = html.replace('https://ui-avatars.com/api/?name=Ajay+Chinthakindi&size=200&background=random', 'profile.jpg')

# Replace CGPA
html = html.replace('CGPA: 7.00', 'CGPA: 6.5')

with open(r'C:\Users\ajayc\Downloads\portfolio1\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
