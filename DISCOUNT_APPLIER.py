def calculate_discount(price, discount_percentage):
    """
    Calculate the discounted price based on the original price and discount percentage.
    only applies the discount if  the discount percentage is 20% or more.
    """
    if discount_percentage >= 20:
        discount_amount = (discount_percentage / 100) * price
        discounted_price = price - discount_amount
        return discounted_price
    else:
        return price
    
 #Prompt the user to enter the price and discount percentage
original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))

#Calculate the discounted price
final_price = calculate_discount(original_price, discount_percentage)
print(f"The final price after discount is: {final_price:.2f}")


