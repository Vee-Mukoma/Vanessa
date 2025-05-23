#Accessing elements in a list
new_list = [1, 2, 3]
result = new_list[2] #uses an index to access the third element
#print(result)

if 1 in new_list:
    print(True)

for n in new_list:
    if n == 1:
        print(True)

        break

#to extend an array
new_list.extend([4, 5, 6])

#to insert an element at the end
new_list.append(7)

#to insert at the beginning and anywhere
new_list.insert(0, 0)

#to remove an element
new_list.remove(2)#removes the first occurrence of 2
