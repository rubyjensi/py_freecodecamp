# Food Delivery Order Dispatch (While inside While)
order_num = 1  
while order_num <= 2:
    print(f"📦 Packaging Order #{order_num}")
    tape_layer = 1  
    while tape_layer <= 3:
        print(f"Applying safety tape layer {tape_layer}...")
        tape_layer += 1      
    print(f"Order #{order_num} sealed and handed over to Rider.\n")
    order_num += 1  