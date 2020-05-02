#Using Python 3.8.0 
#Fist part of my python adventure
"""
#Always a clasic
message = '\nHello world!'
print(message)
print('\n')

#User input
print('But especially to you...')
print("Yes, you... What's your name?")
userName = input()
print('Oh, I see. So... ' + userName + '. Wanna see what I can do?')
print('\n') */
"""
#Instead of commenting each line, use triple commas to comment chunk fo code. 

#Spacebetweenconcepts
spaceCounter = 0
while spaceCounter < 3: 
    print()
    spaceCounter += 1

    #Function for Spacebetweenconcepts. 
def spacer():
    spaceCounter = 0
    while spaceCounter < 3: 
        print()
        spaceCounter += 1    

#Lists
colors = ['Blue','Green', 'Red','Pink']
print(colors)
print(colors[-1])   #-1 Last element of the list.
print(colors[0:-1]) #Second par it's not inclusive. 
print(colors[0:])   #Slicing to the end.
colors.append('Purple') #Adds to the end. 
print(colors)
colors.insert(1,'Yellow') #Add in a position.
print(colors)

bw = ['black', 'white']
colors.append(bw) #This just add a list to the list. A list, inside a list. 
print(colors)
colors.extend(bw) #This truly combines lists. 
print(colors)
colors.remove(bw) #Remove list of 'bw' but not the black and white incorporated with extend. 
print(colors)
colors.remove('Red')
print(colors)
colors.sort() #Alphabetical. 
print(colors)
bw.append('grey')
bw.append('almostgrey')
print(bw)
bw_sorted = sorted(bw) #So we don't alter our bw list. 
print(bw_sorted)

spacer()

#Loops
for color in colors: 
    print(color)

for index,color in enumerate(colors,start=1): #index;position
    print(index, color)

spacer()

numbers = [4,2,1,3,5]

for num in numbers:         #breaks, stops if found. 
    if num == 3:
        print(num,'Found!')
        break
    else:
        print(num)

spacer()

for num in numbers:         #ignores 
    if num == 3:
        continue
    else:
        print(num)

spacer()

#Convert list to string. 
colors_str = '-'.join(colors) #"with -"
print(colors_str)

#Convert string to list on:  "-"
colors_list = colors_str.split('-')
print(colors_list)

spacer()

#Tuples
#Inmutable. 
numbers = (2,3,5,1,4)
print(numbers)

spacer()

#Sets
#No order. 
#Throw away duplicates. 
#Show share values with other sets. 
rgb = {'Red', 'Green','Blue','Blue'}
notrgb = {'Purple','Yellow'}
maybergb = {'Blue', 'Pink'}

print(rgb)
superset = rgb.union(notrgb)
print(superset)
print(rgb.difference(maybergb))

spacer()

#Create an empty set

emptySet = set()
print(emptySet)

spacer()

#Dictionaries

earth = {'element': 'water', 'life': True} #Keys, the key can be almost any data type not just str. 
print(earth.get('element')) #Use get method to access keys, we don't want an error for a reponse if not found. 
print(earth.get('location', 'not found')) #Pass a second arg to display if not found

earth.update({'location':'milky way'}) #Use update method to add. 
print(earth)

removedEarthInfo = earth.pop('location') #Delete but can keep value. 
print(removedEarthInfo)

print(len(earth)) #Numbers of keys. 
print(earth.keys())
print(earth.values())
print(earth.items())

for item in earth: #But this just displays the keys, we cant' do it like a list.  
    print(item)

for key,values in earth.items(): #This is the correct way to access Dictionaries. 
    print(key, values)    

spacer()

#Conditionals


counter = 5
if counter == 0:
    print('No value')
elif counter <=5:
    print('Value is in range: 1-5')
else:
    print('Value is beyond 5')

if 1 == 1 and 2==3: 
    print('Numbers are broken')
else:
    print('Maths are safe!')

#Object identity 'is' Checks same in memory. 

a = [1,2,3]
b = [1,2,3]
print(a == b) #Are values the same? 

print(a is b) #Are they the same? 

print(id(a))
print(id(b))
print(id(a), id(b),sep='-') #Print this way too, interesting. 

#Default false values. 

#False
#None
#Zero for any numeric type
#Any empty sequence, For example: '',[],()
#Any empty mapping: {}

condition = ''

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')






    