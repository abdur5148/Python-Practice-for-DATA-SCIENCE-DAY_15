from operator import itemgetter
list1 = []
while True:
    a = input("\nType 'end' when you done.\nEnter Name,Age,Score : ")
    if a == "end":
        break
    else:
        list1.append(tuple((a.split(","))))
list1.sort(key=itemgetter(0, 1, 2))
print(list1)
