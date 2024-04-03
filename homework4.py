# immutable_var = 1,2,'d','c'
# print(immutable_var)
# immutable_var [0] = 34 # не потдерживает оброщения по элементам
# print(immutable_var)
mutable_list = [1,2,'f','g']
print(mutable_list)
mutable_list[1] = 'a'
print(mutable_list)
mutable_list.append('yes')
print(mutable_list)

