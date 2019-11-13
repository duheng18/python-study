import bs4

soup = bs4.BeautifulSoup(open('example.html'))
spanElem = soup.select('span')[0]

# <span id="author">Al Sweigart</span>
print(str(spanElem))

# author
print(spanElem.get('id'))

# None
print(spanElem.get('some_nonexistent_addr' == None))

# {'id': 'author'}
print(spanElem.attrs)
