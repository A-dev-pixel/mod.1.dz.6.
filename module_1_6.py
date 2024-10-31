# 'module_1_6.py'
my_dict = {"Алексей" : 1991, "Василий" : 1992, "Екатерина": 1990}
print(my_dict)
print(my_dict["Алексей"])
print(my_dict.get("Олег","отсутствующий"))
print(my_dict.update ({"Марк":1992, "Денис" : 1998}))
del my_dict ["Марк"]
print(my_dict)
my_set={1,2,3,4,1,2,3,4,"t","Fort"}
print(my_set)
my_set.update({5,6})
print(my_set)
my_set.remove(5)
print(my_set)