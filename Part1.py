
"""
Created on Thu May 30 16:14:37 2024
@author: Roohi
"""

#%% List
colors = ['red','green','blue']
numbers = [28,14,7,21]
print(colors[-1])
print(numbers[1:3])

colors.append('pink')
numbers.insert(4, 36)
print(colors)
print(numbers)

colors_2=['white','turqoise']
colors.extend(colors_2)
print(colors)
colors.pop()
print(colors)

numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.sort(reverse = True)
print(numbers)
colors.sort()
print(colors)
sorted(colors_2)
print(colors_2)

colors = ['red','green','blue','turqoise']
message = ','.join(colors)
print(message)
message.split(',')
print(message)

# Emty list
numbs_list = []
numbs_list = list()
#%% Loop
for color in colors:
    print(color)
    print(color.count('r'))
    
for index,color in enumerate(colors):
    print(index,color)
#%% Tuple

# Lists are mutable
colors = ['red','green','blue','turqoise']
print(type(colors))
colors[1]='sabz'
print(colors)

# Tuples are immutable
colors_tup= ('red','green','blue','turqoise')
print(type(colors_tup))
colors_tup[1]='sabz'
print(colors)

print(dir(colors_tup))
print(colors_tup.count('blue'))
print(colors_tup.index('blue'))

# Emty tuple
numbs_tup = ()
numbs_tup = tuple()
#%% Set
colors_set = {'red','green','blue','turqoise'}
numbers = [1, 2, 5, 2, 6, 7, 1, 2]
numbers_set = set(numbers)
print(len(numbers))
print(len(numbers_set))


colors_set1 = {'red','green','blue','turqoise'}
colors_set2 = {'whit','black','blue','turqoise'}
print(colors_set1.union(colors_set2))
print(colors_set1.intersection(colors_set2))
print(colors_set1.difference(colors_set2))
print(colors_set2.difference(colors_set1))

# Emty set
numbs_set = {}    #dictionary
numbs_set = set() #set
