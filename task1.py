people = [
    {'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'name': 'Bob', 'age': 22, 'city': 'San Francisco'},
    {'name': 'Charlie', 'age': 35, 'city': 'Los Angeles'}
]
print('Names of people who are above 25:')
ret_age=[]
for name in people:
    if name['age']>25:
        print(name['name'])

people.sort(key=lambda a: a['age'], reverse=True)
for i in people:
    print(i)


