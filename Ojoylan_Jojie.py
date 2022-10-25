print("Catch and eat any of these fruits: ('apple','orange','mango','guava')")
numberOfFruits = int(input("How many fruits would you like to catch? "))
print("Choose a fruit to catch. Press A, O, M, or G.")
basket=[]
for i in range(numberOfFruits):
    f = input("Fruit "+str((i+1))+" of "+str(numberOfFruits)+": ")
    if(f.upper()=='A'):
        basket.append("Apple")
    elif(f.upper()=='O'):
        basket.append("Orange")
    elif(f.upper()=='M'):
        basket.append("Mango")
    elif(f.upper()=='G'):
        basket.append("Guava")
            
print("You basket now has: "+str(basket))
while(len(basket)!=0):
    eat = input("Press E to eat fruit. ")
    if(eat.upper()=='E'):
        basket.pop(len(basket)-1)
    else:
        print("Invalid input")
    if(len(basket)!=0):
        print("Fruit(s) in the basket: "+str(basket))
    else:
        print("No more fruit")