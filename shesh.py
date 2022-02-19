print("hello user")
data = ''
with open('data.txt', 'r', encoding='utf-8') as f:
	for line in f:
		data = data + line

print(data)
s = 'hello'
res = []
while s:
	s = input('INput: ')
	res.append(s)

res = res[:-1]
print(res)

data += '\n'
for x in res:
	data = data + x + '\n'

print(data)

with open('data.txt', 'w', encoding='utf-8') as f:
	f.write(data)