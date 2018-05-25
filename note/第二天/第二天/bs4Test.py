# -*- coding: utf-8 -*-
"""
Created on Sat May 12 16:43:53 2018

@author: Administrator
"""

from bs4 import BeautifulSoup

doc = ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b></p>',
       '<p id="secondpara" align="center">This is paragraph <b>two</b></p></body>',
       '</html>']

#LEGB
soup = BeautifulSoup(''.join(doc), "html.parser")
#print(soup.prettify())
#print(soup)
#print(soup.contents[0])
#myName = soup.contents[0].name
#print(myName) #tag

#<html>
# <head>
#  <title>
#   Page title
#  </title>
# </head>
# <body>
#  <p align="center" id="firstpara">
#   This is paragraph1
#   <b>
#    one
#   </b>
#  </p>
#   <p align="blah" id="secondpara">
#    This is paragraph2
#    <b>
#     two
#    </b>
#   </p>  
# </body>
#</html>


items = soup.findAll('p', align='center')
for i in items:
    print(i['id'])

