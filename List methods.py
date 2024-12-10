animal_list = ['cat','zebra','elephant','dog','panda','gorilla','rabbit','lion']
#(i) Ask the user what index in the list they would like to see, print the animal at that index.
user_index=int(input("What index in the list would you like to see?"))
print(animal_list[user_index])
#(ii) Ask the user what animal they would like to add to the list, add that animal to the list
user_animal=(input("What animal would you like to add to the list?"))
animal_list.append(user_animal)
print(animal_list)
#(iii) Sort the items in alphabetical order and print it to the screen.
animal_list.sort()
print(animal_list)
#(iv) Ask the user to enter an animal.  Print the index of that animal in the list.
user_choice=(input("Enter an animal from the list"))
print(animal_list.index(user_choice))
#(v) Insert “horse” to the list at index 4 (do not overwrite the current animal at index 4)
animal_list.insert(4,'horse')
print(animal_list)
#(vi) Replace the animal at index 2 with “giraffe”.
animal_list.remove(animal_list[2])
animal_list.insert(2,'giraffe')
print(animal_list)
#(vii) Make a copy of the list called animal_list_copy. Sort this list in reverse order and print it to the screen.
animal_list2=animal_list
animal_list2.sort(reverse=True)
print(animal_list2)
#(viii) Loop through the animal_list, printing each animal on a new line.
for i in animal_list:
    print(i)

#	question 2
celebrityList=['Beyonce', 'Lweis Capaldi', 'Ariana Grande','JayZ','Rihanna']
celebrityList.append('Spice Girls')
print(celebrityList)
celebrityList.remove(celebrityList[3])
print(celebrityList)
print(celebrityList.pop(4))
celebrityList.sort()
print(celebrityList)
print()
print()
#QUESTION 3

print("    WElCOME TO OUR ONLINE SHOP   ")
print()
print("The items for sale are: ")
items=["Dinning Table","Dinning chair","Carpet","Rocking chair","Photo frames"]
index=["     0       ","      1      ","  2  ","     3       ","     4       " ]        
print(items)
print(index)

user_list=[]
user_input=int(input("Enter the number of item you are buying:  "))
user_list.append(items[user_input])
      
