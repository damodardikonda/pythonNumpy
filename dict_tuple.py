## Defining an empy set

set_var= set()
print(set_var)
print(type(set_var))

set_var={1,2,3,4,3}


set_var={"Avengers","IronMan",'Hitman'}
print(set_var)
type(set_var)


set_var.add("Hulk")

set1={"Avengers","IronMan",'Hitman'}
set2={"Avengers","IronMan",'Hitman','Hulk2'}

set2.intersection_update(set1)

set2.difference(set1)


set2.difference_update(set1)

print(set2)

dic={}

type(dic)

type(dict())
dict
set_ex={1,2,3,4,5}
type(set_ex)


my_dict={"Car1": "Audi", "Car2":"BMW","Car3":"Mercidies Benz"}
type(my_dict)


my_dict['Car1']


for x in my_dict:
    print(x)


for x in my_dict.values():
    print(x)

for x in my_dict.items():
    print(x)


my_dict['car4']='Audi 2.0'
my_dict

my_dict['Car1']='MAruti'

my_dict

car1_model={'Mercedes':1960}
car2_model={'Audi':1970}
car3_model={'Ambassador':1980}

car_type={'car1':car1_model,'car2':car2_model,'car3':car3_model}
print(car_type)


print(car_type['car1'])

print(car_type['car1']['Mercedes'])


my_tuple=tuple()

type(my_tuple)

my_tuple=()

type(my_tuple)

my_tuple=("Krish","Ankur","John")
my_tuple=('Hello','World')

print(type(my_tuple))
print(my_tuple)

type(my_tuple)
my_tuple.count('Krish')

my_tuple.index('Ankur')
