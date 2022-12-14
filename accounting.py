"Optimizating the customer orders track"

def customer_order_report(order_info): #Defining function that takes one parameter
    elements = line.split("|") # spliting the customer order inf at the separator |
    melon_cost = 1.00 # defining the cost of each melon
    total_melon_bought = float(elements[2]) #getting the amount melon each customer bought and assiging it to the float type
    total_expected = total_melon_bought * melon_cost # calculating the expected price client should pay
    #print(total_expected) # testing the program
    total_customer_paid = float(elements[3]) #getting the value that customer had paid 

    if total_customer_paid != total_expected: #creating the logic to check which customer didnt had done the correct payment
        print(f"{elements[1]} paid ${total_customer_paid},", 
        f"expected ${total_expected:.2f}") # printing a message for the clientes that didnt do the expected payment
        

with open("customer-orders.txt") as customer_orders: # reading the text file and saving the content to the customer_orders variable
    for line in customer_orders.readlines(): #iterating over each line of file
        # print(line) #testing
        customer_order_report(line) #calling the function
        
        
        
         











# for line in customer_orders:
#     if customer_orders[3] != total_expect:
#         print(f"{customer_orders[1]} paid ${customer_orders[3].2f}, expected ${total_expect}.")




# melon_cost = 1.00

# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00



# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )
