import os
f = open('', 'r')
lines = f.readlines()
string = []
for i in range (0, len(lines)):
	line = lines[i].rstrip('\n')
	string.append(line)

dic1 = {}
for index, element in enumerate(string):
	dic1[index] = element

string_name_index = []
for key, values in dic1.items():
	for char in values:
		if char == '>':
			string_name_index.append(key)
string_name_index.append(len(lines))

dic2 = {}
for i in range(0, len(string_name_index) - 1):
	dna_string = ''
	for n in range(string_name_index[i] + 1, string_name_index[i + 1]):
		dna_string += dic1[n]
	dic2[dic1[string_name_index[i]].lstrip('>')] = dna_string
f.close()
t = open(, 'w')
print (dic2, file = t)
