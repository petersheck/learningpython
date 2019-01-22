D1 = { 'name': 'Bob', 'age': 40}
print(D1)
D2 = { 'CTO' : D1}
print(D2)
D3 = dict(name = 'Bob', age = 40)
print(D3)
D4 = dict([('name', 'Bob'), ('age', 40)])
print(D4)
print(D4['name'])
print(D2['CTO']['age'])
print(D4.keys())
print(D4.values())
print(D4.items())
print(D4.get('name'))
D4['money'] = 5000
print(D4)
for key in D4.keys():
    print(key + '\t' + str(D4[key]))

