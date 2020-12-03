file = open('hello.txt', 'w')
file.write('Hello, world!')
file.close()

file = open('hello.txt', 'r')
s = file.read()
print(s)
file.close()

with open('hello.txt', 'w') as file:
    for i in range(3):
        file.write('Hello, world! {0}\n'.format(i))

lines = ['안녕\n', '난\n', '멋쟁이야\n']
with open('hello.txt', 'w') as file:
    file.writelines(lines)

with open('hello.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

with open('hello.txt', 'r') as file:
    line = None
    while line != '':
        line = file .readline()
        print(line.strip('\n'))

with open('hello.txt', 'r') as file:
    for line in file:
        print(line.strip('\n'))


import pickle

name = 'james'
age = 17
address = '반포동'
scores = {'korean': 90, 'english': 95}

with open('james.p', 'wb') as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)

with open('james.p', 'rb') as file:
    print(pickle.load(file))
    print(pickle.load(file))
    print(pickle.load(file))
    print(pickle.load(file))


with open('words.txt', 'r') as file:
    words = file.readline()
    sss = words.split()
    for s in sss:
        s = s.strip(',.')
        if 'c' in s:
            print(s)


