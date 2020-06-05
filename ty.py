x=[1,2,'a',4,'c'];
print(x)

print(type(x))

x.append(3.4)
print(x)

for i in x:
    print(i)

i=0;
while i<len(x):
    print(x[i]);
    i=i+1

print([1,2]+[3,4])
print([1+2],[3+4])
print([2]*3)

x = 'This is a string'
print(x[-4:-2])

f="abcdefg"
print("abc" in f)

first="my name is Damodar".split()[2:];
print(first)

print('chris'+str(2))

x={1:'a',2:'b',3:'c','d':'e'}
print(x[1])
print(x['d'])

x[f]=7
print(x[f])

for i in x:
    print(x[i])



d = {'a': 1, 'b': 2}
print(d)
d['a'] = 100  # existing key, so overwrite
d['c'] = 3  # new key, so add
d['d'] = 4
print(d)

x=('damodar','dikonda','damu@dikonda');
first, last, email=x
print(first)
print(email)



sales_record = {
'price': 3.24,
'num_items': 4,
'person': 'Chris'}

sales_statement = '{} bought {} item(s) at a price of {} each for a total of {}'

print(sales_statement.format(sales_record['person'],
                             sales_record['num_items'],
                             sales_record['price'],
                             sales_record['num_items']*sales_record['price']))
