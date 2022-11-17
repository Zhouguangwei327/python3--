# 1、对象和数组

date = """
[
    {
        "name": "Bob",
        "gender": "male",
        "age": 11
    },
    {
        "name": "Selina",
        "gender": "female",
        "age": 12
    }
]
"""

# 2、读取json
import json

print(type(date))
date = json.loads(date)
print(type(date))


name1 = date[0].get('name')
name2 = date[1].get('name')
print(name1, name2)
