import re

with open('C:/Users/ajayc/Downloads/portfolio1/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Contact Number
html = html.replace('tel:+919364356789', 'tel:+918247605336')
html = html.replace('+91 93643 56789', '+91 8247605336')

# Replace Email
html = html.replace('saitanmai6969@gmail.com', 'ajaychinthakindi25@gmail.com')

# Replace Download Resume
html = html.replace('Mockdrive%20CV%20(1)%20(1)%20(1)%20(1)%20(1).pdf', '#')

# Replace Github link in social icons
html = html.replace('https://github.com/VSaiTanmai', 'https://github.com/Ajavchinthakindi')

# Replace Linkedin link in social icons
html = html.replace('https://www.linkedin.com/in/saitanmai/', 'https://linkedin.com/in/chinthakindi-ajay-980244283/')

with open('C:/Users/ajayc/Downloads/portfolio1/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
