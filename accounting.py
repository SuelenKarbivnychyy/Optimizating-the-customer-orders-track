"Optimizating the customer orders track"

def customer_order_report(order_info):
    elements = line.split("|")
    melon_cost = 1.00
    total_melon_bought = float(elements[2])
    total_expected = total_melon_bought * melon_cost
    #print(total_expected)
    total_customer_paid = float(elements[3])

    if total_customer_paid != total_expected:
        print(f"{elements[1]} paid ${total_customer_paid},",
        f"expected ${total_expected:.2f}")
        

with open("customer-orders.txt") as customer_orders:
    for line in customer_orders.readlines():
        # print(line)
        customer_order_report(line)
        
        
        
         











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
