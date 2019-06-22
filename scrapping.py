# pip install requests BeautifulSoup 
import requests
from bs4 import BeautifulSoup

page = 1
print("start scrapping...")

while page < 10 :

    # Loops in all page between 1 and 9
    result = requests.get('http://quotes.toscrape.com/page/' + str(page) + '/')
    # Parse content to html
    soup = BeautifulSoup(result.text, "html.parser")

    # Get all div with class quote
    divs = soup.find_all('div', class_ = 'quote')

    for div in divs:
        tags = []
        # Get author in second span and find small
        author = div.findAll('span')[1].find('small').text
        # Get description in first span
        description = div.findAll('span')[0].text

        # Get tags in a attribute from div
        arrayTags = div.find('div').findAll('a')
        for tag in arrayTags:
            # Insert tag founded in arrayTags
            tags.append(tag.text)        

    page += 1

print("end scrapping...")