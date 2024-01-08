# 1
amino_list = ["Try", "Asp", "Lys", "Met"]
print(amino_list)
plus = 4
for i in range(4):
    plus = plus - 1
    print(amino_list[plus])
# 2
amino_list2 = ["Try", "Asp", "Lys", "Met"]
new_list = amino_list2.append('Asp')
print(amino_list2)
sorter = amino_list2.sort()
print(amino_list2)
sorter2 = amino_list2.sort(reverse=True)
print(amino_list2)
sorter3 = amino_list2[2:4]
print(sorter3)

# 3
new_list2 = ["Trp", "Arg", "Liu", "Ilu", "Asp"]
g = len(new_list2)
user = int(input('Enter a number from one to five'))
if user <= 5:
    print(new_list2[user])
else:
    print("Error message")


