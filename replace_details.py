import os
import re

file_path = r"c:\Users\ajayc\Downloads\raghu portfolio\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# Replace Names
text = text.replace("AjayChinthakindi", "Korada Raghu Ram")
text = text.replace("Chinthakindi Ajay", "Korada Raghu Ram")
text = text.replace("Ajay Chinthakindi", "Korada Raghu Ram")

# Using regex for standalone word Ajay if needed. 
text = re.sub(r'\bAjay\b', 'Raghu Ram', text)

# Replace Email
text = text.replace("ajaychinthakindi25@gmail.com", "raghuramkorada13@gmail.com")

# Replace Phone Number
# We can search for phone numbers in the format 8247605336 or +91 8247605336
text = text.replace("8247605336", "8309615949")
text = text.replace("+91 8247605336", "+91 8309615949")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Replacement Complete")
