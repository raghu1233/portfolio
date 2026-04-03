from bs4 import BeautifulSoup
with open(r"c:\Users\ajayc\Downloads\raghu portfolio\index.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

for h2 in soup.find_all('h2'):
    print("H2:", h2.text.strip())

for h3 in soup.find_all('h3'):
    print("H3:", h3.text.strip())
