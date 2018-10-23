# this program gets an items original price and 
# calculates its sales price, with a 20% discount

# Get the items original price 
original_price = float(input("Enter the item's original price: "))

# Calculate the amount of the discount.
discount = original_price * 0.2

# Calculate the sale price.
sale_price = original_price - discount

# display the sale price.
print('The sale price is', sale_price)
