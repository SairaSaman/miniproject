import csv
main_menu = ("""
Main Menu
0. Exit the app
1. Products menu
2. Couriers menu
3. Orders menu """)

products_menu = ("""  
Products Menu
0. Go to main menu
1. List of products
2. Add a new product
3. Remove a product
4. Update a product """)

couriers_menu = ("""
Couriers Menu
0. Go to main menu
1. List of couriers
2. Add a new courier
3. Remove a courier
4. Update a courier """)

orders_menu = ("""
Couriers Menu
0. Go to main menu
1. List of orders
2. Add a new order
3. Update status of an order
4. Update an order
5. Remove an order  """)

order_status = ("""
Order Status
1. Ready
2. Out for delivery
3. Delay """)


#Read a csv file 
import csv
def read_file_csv (file_name):
    try:
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file, delimiter = ',')
            return list(reader)
    except FileNotFoundError:
        msg =  "Sorry, the file "+ file_name + " does not exist."    
        print(msg)

#Format list with index starting from 1
def display_contents_csv (input_list):
    display_contents = ""
    for index,item in enumerate(input_list):
        display_contents += f'{index+1}.{item}\n'
    return (display_contents)

#Function for append dictionary/ add to the csv file
def add_file_csv (file_name,field_names,add_item):
    with open( file_name, 'a', newline='') as file:
        dictwriter_object = csv.DictWriter(file, fieldnames = field_names)
        dictwriter_object.writerow(add_item)

#Function to remove from dictionary/ write to csv file
def write_file_csv (file_name,field_names,remove_item):
    with open (file_name, 'w', newline='') as file:
        product_writer = csv.DictWriter(file, fieldnames = field_names)
        product_writer.writeheader()
        product_writer.writerows(remove_item)



while True:
    print(main_menu)
    user_input_main = int(input('Enter an option: '))
    if user_input_main == 0:
        break # exit the app
    elif user_input_main == 1: #Bring the sub menu
        while True:
            print(products_menu)
            user_input_products= int(input("Please enter an option from above:"))

            if user_input_products == 0: #Go to main menu
                break #go to main menu

            elif user_input_products ==1: #Display products
                print('Products')
                products = read_file_csv('products.csv')
                print(display_contents_csv(products))
            
            elif user_input_products ==2: #Add a new product

                input_product_name = input("Enter new product: ")
                input_product_price = input("Enter the price of the product: ")

                product_add = {
                            "product_name" : input_product_name,
                            "price": input_product_price,
                        }
                append_field_names = ['product_name', 'price']

                add_file_csv('products.csv',append_field_names,product_add)

            elif user_input_products ==3: #Remove a product
                products = read_file_csv('products.csv',)
                print(display_contents_csv(products))

                input_delete_product = int(input('Enter the corresponding index of order to delete: '))
                del products[input_delete_product-1]

                product_deleted = products

                field_names = ('product_name', 'price')

                write_file_csv('products.csv', field_names, product_deleted)
                    

            elif user_input_products == 4: #Update a product
                products = read_file_csv('products.csv')
                print(display_contents_csv(products))

                input_index_product = int(input ('Please choose corresponding index of the product: '))
                input_new_product = input("Enter the product name: ")
                input_new_price = input("Enter the price: ")

                products[input_index_product-1]['product_name'] = input_new_product
                products[input_index_product-1]['price'] = input_new_price

                list_update = products

                product_fieldnames = ['product_name', 'price']

                write_file_csv('products.csv', product_fieldnames, list_update)

    elif user_input_main == 2: #Couriers menu selected
        while True:
            print(couriers_menu)
            user_input_couriers = int(input('Please choose from above options: '))

            if user_input_couriers == 0:
                break #Go to main menu

            elif user_input_couriers == 1: #Display the couriers
                print('Couriers list')
                couriers = read_file_csv('couriers.csv')
                print(display_contents_csv(couriers))

            elif user_input_couriers == 2: #Add new courier
                input_courier_name = input("Enter new courier: ")
                input_courier_phone = input("Enter phone no. : ")

                courier_add = {
                            "courier_name" : input_courier_name,
                            "phone": input_courier_phone,
                        }

                append_field_names = ['courier_name','phone']


                add_file_csv('couriers.csv',append_field_names,courier_add)
            
            elif user_input_couriers ==3: #Remove a courier
                couriers = read_file_csv('couriers.csv')
                print(display_contents_csv(couriers))

                input_delete_courier = int(input('Enter the corresponding index of courier to delete: '))
                
                del couriers[input_delete_courier-1]

                courier_delete = couriers

                field_names_couriers = ['courier_name','phone']

                write_file_csv('couriers.csv', field_names_couriers,courier_delete )


        
            elif user_input_couriers == 4: #Update a courier
                couriers = read_file_csv('couriers.csv')
                print(display_contents_csv(couriers))

                input_index_courier = int(input ('Please choose corresponding index of the courier: '))
                input_new_courier = input("Enter the courier's name: ")
                input_new_phone = input("Enter phone no.: ")

                couriers [input_index_courier-1]['courier_name'] = input_new_courier
                couriers [input_index_courier-1]['phone'] = input_new_phone

                field_names_couriers = ['courier_name', 'phone']

                list_couriers = couriers
                
                write_file_csv('couriers.csv',field_names_couriers,list_couriers)


    elif user_input_main == 3: #Open orders
        while True:
            print(orders_menu)
            user_input_orders = int(input('Please enter an option from above: '))

            if user_input_orders == 0:
                break #go to main menu

            elif user_input_orders == 1: #Display orders
                orders = read_file_csv('orders.csv')
                print(display_contents_csv(orders))

            elif user_input_orders == 2: #Add an order
                input_name = input("Enter customer's name: ")
                input_address = input("Enter the customer's address: ")
                input_phone = input("Enter the customer's phone: ")
                
                #print list of products
                products = read_file_csv('products.csv')
                print('Products list')
                print(display_contents_csv(products))
                input_products_order = input('Enter corresponding indices of the products: ')

                #print couriers
                print('Couriers list')
                couriers = read_file_csv('couriers.csv')
                print(display_contents_csv(couriers))
                input_courier = input("Enter the corresponding index of the courier: ")
                
                #convert to list
                input_products = input_products_order.split (",")
                # convert each element as integers
                products_order_list = []
                for i in input_products:
                    products_order_list.append(int(i))


                new_order = {
                    "customer_name" : input_name,
                    "customer_address": input_address,
                    "customer_phone": input_phone,
                    "products_order" : products_order_list,
                    "courier" : input_courier,
                    "status": "Preparing"
                }

                order_add_fieldnames = ['customer_name','customer_address','customer_phone', 'products_order','courier','status']

                add_file_csv('orders.csv',order_add_fieldnames,new_order)
            
                print('New order add.')
            
            elif user_input_orders == 3:#Update status of an order
                orders = read_file_csv('orders.csv')
                print(display_contents_csv(orders))

                input_index = int(input ('Please choose the corresponding index of order: '))
                    #print the list of status with index
                print(order_status)
                input_status = int(input("Please choose index of the status: ")) 
                if input_status == 1:
                    orders[input_index-1]['status'] = 'Ready'
                elif input_status == 2:
                    orders[input_index-1]['status'] = 'Out for delivery'
                elif input_status == 3:
                    orders[input_index-1]['status'] = 'Delay'
                
                order_list = orders

                order_fieldnames = ['customer_name','customer_address','customer_phone', 'products_order','courier','status']
                
                write_file_csv('orders.csv',order_fieldnames,order_list)

            elif user_input_orders == 4:#update existing order
                orders = read_file_csv('orders.csv')
                print(display_contents_csv(orders))

                input_index = int(input ('Please choose the corresponding index of order: '))
                
                print('Update order', input_index)

                input_name = input("Enter the customer name: ")
                input_address = input("Enter customer's address: ")
                input_phone = input ("Enter the phone no.: ")
                input_products_order = input("Enter products: ")
                input_courier = input("Enter courier index: ")
                input_status = input("Enter status: ")

                input_products = input_products_order.split (",")
                products_order_list = []
                for i in input_products:
                    products_order_list.append(int(i))


                if input_name == '':
                    pass
                else:
                    orders[input_index-1]['customer_name'] = input_name

                if input_address == '':
                    pass
                else:
                    orders[input_index-1]['customer_address'] = input_address

                if input_phone == '':
                    pass
                else:
                    orders[input_index-1]['customer_phone'] = input_phone

                if input_products == '':
                    pass
                else:
                    orders[input_index-1]['products_order'] = products_order_list

                if input_courier == '':
                    pass
                else:
                    orders[input_index-1]['courier'] = input_courier

                if input_status == '':
                    pass
                else:
                    orders[input_index-1]['status'] = input_status

                list_order = orders

                order_fieldnames = ['customer_name','customer_address','customer_phone', 'products_order','courier','status']

                write_file_csv('orders.csv',order_fieldnames,list_order)


            elif user_input_orders == 5:#Delete an order
                orders = read_file_csv('orders.csv')
                print(display_contents_csv(orders))

                input_delete_order = int(input('Enter the corresponding index of order to delete: '))

                del orders[input_delete_order-1]
                    
                order_deleted = orders
                print('Order deleted at index:',input_delete_order)

                order_fieldnames = ['customer_name','customer_address','customer_phone', 'products_order','courier','status']


                write_file_csv('orders.csv',order_fieldnames,order_deleted)


    else:
        print('Invalid input')

print('Adios Amigos!!')