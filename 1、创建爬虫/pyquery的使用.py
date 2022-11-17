from pyquery import PyQuery as pq

html = '''
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span class='link2'>Elsie1</span>
                <span class='link2'>Elsie2</span>
                <span class='link2'>Elsie3</span>
            </a>
            Hello
            <a href="http://example.com/elsie" class="sister" id="link3">Lacie</a>
            and
            <a href="http://example.com/title" class="sister" id="link4">Tillie</a>
            and they lived at the bottom if a well
        </p>
    </body>
</html>
'''

# doc = pq(url='https://www.baidu.com', encoding = 'utf-8')
# doc = pq(filename='./test.html')
doc = pq(html)
# print(doc('a'))
items = doc('#link1 .link2 ')
print(type(items))
print(items)
lis = items.find('span')
print(lis)

# for item in doc('#link1 .link2').items():
#     print(item.text())

