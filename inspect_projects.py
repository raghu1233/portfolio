from bs4 import BeautifulSoup
import sys

with open(r"c:\Users\ajayc\Downloads\raghu portfolio\index.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

print("=== FIRST PROJECT ===")
h2_proj = soup.find(lambda t: t.name == 'h2' and 'RecentProjects' in t.text)
if h2_proj:
    section = h2_proj.parent
    if section:
        # Find first element that looks like a card
        card = section.find('div', recursive=True)
        if card:
            # let's just find the first .project-card or similar
            cards = section.find_all('div', class_=lambda c: c and 'project' in c)
            if cards:
                print(cards[0].prettify()[:2000])
            else:
                print(section.prettify()[:2000])

print("\n=== FIRST ACADEMIC ITEM ===")
h2_acad = soup.find(lambda t: t.name == 'h2' and 'AcademicJourney' in t.text)
if h2_acad:
    section = h2_acad.parent
    if section:
        items = section.find_all('div', class_=lambda c: c and ('item' in c or 'card' in c or 'edu' in c))
        if items:
            print(items[0].prettify()[:2000])
        else:
            print(section.prettify()[:2000])
