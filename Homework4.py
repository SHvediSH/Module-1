immutable_var = (1, 2, True, 'war') #Создание переменной типа "кортеж"
print (immutable_var)

#immutable_var [0] = 300            #Объекты типа tuple (кортеж) не поддерживают обращение по элементам

immutable_var2 = ([1, 2], 0)        #Создание "кортежа" с подсписком внутри
print(immutable_var2)

immutable_var2 [0][0] = 200         #Можно изменять часть содержимого в кортеже используя в нем ссылки на объекты
print (immutable_var2)

mutable_list = [1, True, 'nigga']   #Обыкновенный список поддерживающий изменения в процессе написания кода
print(mutable_list)

mutable_list[0] = 69                #Изменение списка путём присвоения нового значения первому элементу списка
print (mutable_list)