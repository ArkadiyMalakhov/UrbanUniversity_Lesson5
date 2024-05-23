immutable_var = 1, 2, 3, "Four", "Five", True
print(immutable_var)
# immutable_var[3] = 4
# print(immutable_var)
# Tип данных tuple не поддерживает изменение объектов содержащихся в нем,
# если объекты относятся к неизменяемому типу данных
mutable_var = [1, 2, 3, "Four", "Five", True]
mutable_var[3] = 4
print(mutable_var)
