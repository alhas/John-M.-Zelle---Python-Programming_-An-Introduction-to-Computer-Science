def konditorei():

    order = float(input("Please write order cost: "))

    cent = 0.01
    fixed_cost = 1.50
    shipping_cost_for_every_pound = 0.86
    shipping_cost_for_every_cent = shipping_cost_for_every_pound * cent
    order_as_Cent = order / cent

    shippingCost_as_Pound = (shipping_cost_for_every_cent * order_as_Cent)
    
    print(shippingCost_as_Pound)
    print(order + shippingCost_as_Pound + fixed_cost  )    


konditorei()