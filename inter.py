list = [1,0,2,0,4,6]
for item in list:
    if item==0:
        list.remove(item)
        list.append(item)
print(list)