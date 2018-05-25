# -*- coding: utf-8 -*-
"""
Created on Sat May 12 16:01:12 2018

@author: Administrator
"""

from lxml import etree

xml = """<bookstore>
	<book>
		<title lang="en">Harry Potter</title>
		<price>29.99</price>
		<pageNumer>102</pageNumer>
	</book>
	<book>
		<title lang="ch">Python爬虫</title>
		<price>39.9</price>
	</book>
</bookstore>
"""

root = etree.fromstring(xml)
print(root) #<Element bookstore at 0xa6af6c8>

# book element
#c1 = root.getchildren()[0]
#cc1 = c1.getchildren()[0]
#cc1c = c1.getchildren()[2]
#print(cc1.text)
#print(cc1.attrib)
#print(cc1c.text)
#
#c2 = root.getchildren()[1]
#cc2 = c2.getchildren()[0]
#print(cc2.text)
#print(cc2.attrib)

# 不关心节点层次关系的细节，取属性
#elements = root.xpath("//@lang")
#print(elements)

# 取price的text信息
priceElements = root.xpath("/bookstore/book[price>35]/title")
for i in priceElements:
    print(i.text)
