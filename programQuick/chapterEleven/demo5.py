import bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select('#author')
# <class 'list'>
# print(type(elems))

# 1
# print(len(elems))

# [<span id="author">Al Sweigart</span>]
# print(elems)

# <span id="author">Al Sweigart</span>
# print(str(elems[0]))

# Al Sweigart
# print(elems[0].getText())

# {'id': 'author'}
# print(elems[0].attrs)

pElems = exampleSoup.select('p')
# 3
# print(len(pElems))

# <p>Download my <strong>Python</strong> book from <a href="http:// inventwithpython.com">my website</a>.</p>
# print(str(pElems[0]))

# Download my Python book from my website.
# print(pElems[0].getText())

# <p class="slogan">Learn Python the easy way!</p>
# print(str(pElems[1]))

# Learn Python the easy way!
# print(pElems[1].getText())

# <p>By <span id="author">Al Sweigart</span></p>
# print(str(pElems[2]))

# By Al Sweigart
print(pElems[2].getText())
