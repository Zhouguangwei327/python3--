from parsel import Selector

html = '''
    <html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            Hello
            <a href="http://example.com/elsie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/title" class="sister" id="link3">Tillie</a>
            and they lived at the bottom if a well
        </p>
    </body>
</html>
'''
selector = Selector(text=html)
items = selector.css('.sister')
print(len(items), type(items), items)