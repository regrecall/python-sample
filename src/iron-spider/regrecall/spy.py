from urllib2 import urlopen, HTTPError
from bs4 import BeautifulSoup
import re

# def getTitle(url):
#     try:
#         html = urlopen(url)
#     except HTTPError as e:
#         print(e)
#         return None
#     try:
#         bsObj = BeautifulSoup(html.read(), "html.parser")
#         title = bsObj.body.h1
#     except AttributeError as e:
#         print(e)
#         return None
#     return title
#
#
# title = getTitle("http://www.pythonscraping.com/pages/page1.html")
# if title == None:
#     print("Title could not be found")
# else:
#     print(title)
#
# htmlTag = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
# bsTag = BeautifulSoup(htmlTag.read(), "html.parser")
#
# tagList = bsTag.findAll("span", {"class": "green"})
# for name in tagList:
#     print (name.get_text())
#
# nameList = bsTag.findAll(text="the prince")
# print(len(nameList))
#
htmlChildren = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsChildren = BeautifulSoup(htmlChildren.read(), "html.parser")

# for child in bsChildren.find("table", {"id": "giftList"}).children:
#     print(child)

# for sibling in bsChildren.find("table", {"id": "giftList"}).tr.next_siblings:
#     print(sibling)

# print(bsChildren.find("img", {"src": "../img/gifts/img1.jpg"})).parent.previous_sibling.get_text()

images = bsChildren.findAll("img", {"src": re.compile("\.\./img\/gifts/img.*\.jpg")})
for image in images:
    print(image["src"])

print(bsChildren.findAll(lambda tag: len(tag.attrs) == 2))