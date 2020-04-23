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