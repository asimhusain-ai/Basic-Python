set1 = {1, 2, 3, 4, 5}
print("Set Is:- ",set1)
set1.add(6)
print("Set After Addition:- ",set1)
set1.remove(3)
print("Set After Subtraction:- ",set1)
present = 4 in set1
length = len(set1)
set2 = {4, 5, 6, 7, 9}
print("Set Is:- ",set2)
union = set1.union(set2)
intersection = set1.intersection(set2)
difference = set1.difference(set2)
is_subset = set1.issubset(set2)
print("Is 4 Present:- ", present)
print("Set Length:- ", length)
print("Union Set:- ", union)
print("Intersection Set:- ", intersection)
print("Difference Set:- ", difference)
print("Is set1 a subset of set2:- ", is_subset)
