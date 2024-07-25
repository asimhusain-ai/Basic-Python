dict = {1:'Asim',
        2:'Hina',
        3:'Zishan',
        4:'Yahiya'
        }
copied = dict.copy()
print("Actual Dictionary:- ",dict)
print(dict.get(1))
print("Length: ",len(dict))
dict[3]='Arbaz'
print("Updated Dictionary:- ",dict)
print(dict.pop(4))
present = "Asim" in dict
print(present)
print(dict.clear())
print(copied)