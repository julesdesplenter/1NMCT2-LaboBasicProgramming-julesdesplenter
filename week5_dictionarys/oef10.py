set = {8500, 4523}

print(set)
set.update({4561})
print(set)
set.update({8500})
print(set)
# je kan geen 2 dezelfde elementen hebben in set
# set[{'8500'}] in een set heeft geen vaste plaats
set.remove(8500)
print(set)
