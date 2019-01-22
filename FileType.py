input = open('data.txt', 'r')
for line in input:
    print(line),
print
input.close()
name = dict(first='Bob', last='Smith')
rec = dict(name=name, job=['dev', 'mgr'], age=40.5)
import json
S = json.dumps(rec)
output = open('data.json', 'w')
output.write(S)
output.close()
readit = open('data.json', 'r')
for line in readit:
    print(line),
print
json.dump(rec, fp=open('testjson.txt', 'w'), indent=4)
print(open('testjson.txt').read())
P = json.load(open("testjson.txt"))
print(P)


