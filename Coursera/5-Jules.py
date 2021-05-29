class ClassName:
    pass

new_object = ClassName()

print (type(new_object))

my_list = [1,
           1.2,
           "1.2",
           (1.2),
            [1,2],
            {1:2}]

my_list.append(new_object)

for item in my_list:
    print (item, ":", type(item))



