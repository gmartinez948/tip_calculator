    
#Creating a tip calculator with a split pay function.

#Tip calculator will calculate meal price + tip + tax and split it between the amount of guests 

print("Welcome to my Tip Calculator")

# variable for tax
tax = 10 / 100

# Storing a value for meal as a float that requires input from the user.
price = float(input("What is the price of your meal?: "))

# Identifying a variable to split the bill amongst members of the group
party_group = int(input("How many people are in your group?: "))

# Creating a variable that will serve as the tip amount and is discretional to the user. 
tip = int(input("How much would you like to tip? Please enter a whole number as your percentage: "))

# This variable converts the integer to a float
total_tip = tip / 100

# Variables that calculate the full meal price
meal_after_tax = price + (price * tax)
total_price = (meal_after_tax * total_tip) + meal_after_tax

# Looping through possible tip inputs and then dividing them per person in party_group
if tip >= 1:
    for t in range(1, tip): 
        print(f"Your party's total is {total_price} and {total_price / party_group} per person!") 
        break
else:
    print(" You did not enter a valid tip percentage")


# Finished


        
