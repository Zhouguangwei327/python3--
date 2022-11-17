from lxml import etree



html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[contains(@class, li) and @name="item"]/a/text()')
print(result)