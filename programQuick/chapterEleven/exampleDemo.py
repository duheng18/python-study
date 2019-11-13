import bs4

exampleFile = open('example.html')

# eF: <class '_io.TextIOWrapper'>
# print('teF:', type(exampleFile))

# eF: <_io.TextIOWrapper name='example.html' mode='r' encoding='UTF-8'>
# print('eF:', exampleFile)

exampleSoup = bs4.BeautifulSoup(exampleFile.read())

# eS: <!-- This is the example.html example file. --><html>
# print('eS:', exampleSoup)

elems = exampleSoup.select('#author')

# te: <class 'list'>
# print('te:', type(elems))

# le: 1
# print('le:', len(elems))

# <class 'bs4.element.Tag'>
# print(type(elems[0]))

# <span id="author">Al Sweigart</span>
# print(str(elems[0]))

# {'id': 'author'}
# print(elems[0].attrs)

# Al Sweigart
# print(elems[0].getText())

pElems = exampleSoup.select('p')
# 3
# print(len(pElems))

# <p>Download my <strong>Python</strong> book from <a href="http:// inventwithpython.com">my website</a>.</p>
# print(str(pElems[0]))

# Download my Python book from my website.
# print(pElems[0].getText())

# <p>Download my <strong>Python</strong> book from <a href="http:// inventwithpython.com">my website</a>.</p>
# print(str(pElems[0]))

# Learn Python the easy way!
# print(pElems[1].getText())

# <p class="slogan">Learn Python the easy way!</p>
# print(str(pElems[1]))

# By Al Sweigart
# print(pElems[2].getText())

# <p>By <span id="author">Al Sweigart</span></p>
# print(str(pElems[2]))
