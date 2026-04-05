from os import remove

number_list = [1,2,3,4,5]
print(number_list)

#pop
#pop por defecto elimina el index -1 o si le pasamos por parametro un index borra ese
print(number_list.pop())
print(number_list.pop(2))
print(number_list)

# remove

number_list.remove(4)
print(number_list)


#clear
number_list.clear()
print(number_list)
