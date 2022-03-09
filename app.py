#Import pymysql,os and load_ditenv
import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(
    host,
    user,
    password,
    database
)

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

print("-------------------------------------------")
print("             Cafe Brin2                    ")
print("-------------------------------------------")

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
                cursor = connection.cursor()
                cursor.execute('SELECT * FROM products')
                # Gets all rows from the result
                rows = cursor.fetchall()
                for row in rows:
                    print(f'Product_id:{str(row[0])}, Name: {str(row[1])}, Price: {row[2]}')
                cursor.close()

            elif user_input_products ==2: #Add a new product
                input_product_name = input("Please enter product name: ")
                input_product_price = input("Please enter product price: ")
                
                cursor = connection.cursor()
                sql = ("INSERT INTO products (name,price) Values (%s,%s)")
                val = [(input_product_name, input_product_price)]
                cursor.executemany(sql,val)
                connection.commit()
                cursor.close()

            elif user_input_products ==3: #Remove a product
                cursor = connection.cursor()
                cursor.execute('SELECT * FROM products')
                rows = cursor.fetchall()
                for row in rows:
                    print(f'Product_id: {row[0]}, Name: {row[1]}, Price: {row[2]}')
                #Ask for the product to be removed
                input_product_id = int(input ("Please enter the id no. of product to delete: "))
                
                sql_1 = ('DELETE FROM order_products WHERE product_id =%s')
                sql = ('DELETE  FROM products WHERE product_id = %s')
                val = [(input_product_id)]
                
                cursor.executemany(sql_1,val)
                cursor.executemany(sql,val)
                connection.commit()
                cursor.close()

            elif user_input_products == 4: #Update a product
                cursor = connection.cursor()
                cursor.execute('SELECT * FROM products')
                rows = cursor.fetchall()
                for row in rows:
                    print(f'Product_id: {row[0]}, Name: {row[1]}, Price: {row[2]}')

                input_product_id = int(input ('Please choose corresponding id of the product: '))
                input_new_product = input("Enter the product name: ")
                input_new_price = input("Enter the product price: ")

                if input_new_product == "":
                    pass
                else:
                    sql = ("UPDATE products SET name = %s WHERE product_id = %s")
                    val = [(input_new_product, input_product_id)]
                    cursor.executemany(sql,val)
                    connection.commit()
                    

                if input_new_price == "":
                    pass
                else:
                    sql = "UPDATE products SET price = %s WHERE product_id = %s"
                    val = [(input_new_price, input_product_id)]
                    cursor.executemany(sql,val)
                    connection.commit()
                    
                cursor.close()

            else:
                print("Invalid input.")

    elif user_input_main == 2: #Couriers menu selected
        while True:
            print(couriers_menu)
            user_input_couriers = int(input('Please choose from above options: '))

            if user_input_couriers == 0:
                break #Go to main menu

            elif user_input_couriers == 1: #Display the couriers
                cursor = connection.cursor()
                cursor.execute('SELECT * FROM couriers')
                rows = cursor.fetchall()
                for row in rows:
                    print(f'Courier id:{str(row[0])}, Name: {str(row[1])}, Phone: {row[2]}')

            elif user_input_couriers == 2: #Add new courier
                input_courier_name = input("Please enter courier name: ")
                input_courier_phone = input("Please enter courier phone: ")
                
                cursor = connection.cursor()
                
                sql = ("INSERT INTO couriers (name,phone) Values (%s,%s)")
                val = [(input_courier_name, input_courier_phone)]
                
                cursor.executemany(sql,val)
                connection.commit()
                cursor.close()

        
            elif user_input_couriers ==3: #Remove a courier
                cursor = connection.cursor()
                cursor.execute('SELECT * FROM couriers')
                rows = cursor.fetchall()
                for row in rows:
                    print(f'Courier id:{str(row[0])}, Name: {str(row[1])}, Phone: {row[2]}')

                input_courier_id = int(input ("Please enter the id no. of courier to delete: "))

                
                sql_1 = ('DELETE FROM order_couriers WHERE courier_id =%s')
                sql = ("DELETE  FROM couriers WHERE courier_id = %s")
                val = [(input_courier_id)]

                cursor.execute(sql_1,val)
                cursor.execute(sql,val)
                connection.commit()
                cursor.close()

            elif user_input_couriers == 4: #Update a courier
                cursor = connection.cursor()
                cursor.execute('SELECT * FROM couriers')
                rows = cursor.fetchall()
                for row in rows:
                    print(f'Courier id:{str(row[0])}, Name: {str(row[1])}, Phone: {row[2]}')

                input_id_courier = int(input ('Please choose corresponding id of the courier: '))
                input_name_courier = input("Enter the courier's name: ")
                input_phone_courier = input("Enter the phone no.: ")

                if input_name_courier == "":
                    pass
                else:
                    sql = ("UPDATE couriers SET name = %s WHERE courier_id = %s")
                    val = [(input_name_courier,input_id_courier)]
                    cursor.executemany(sql,val)
                    connection.commit()

                if input_phone_courier == "":
                    pass
                else:
                    sql = ("UPDATE couriers SET phone = %s  WHERE courier_id = %s")
                    val = [(input_phone_courier, input_id_courier)]
                    cursor.executemany(sql,val)
                    connection.commit()
                cursor.close()
            else:
                print("Invalid input.")

    elif user_input_main == 3: #Open orders
        while True:
            print(orders_menu)
            user_input_orders = int(input('Please enter an option from above: '))

            if user_input_orders == 0:
                break #go to main menu

            elif user_input_orders == 1: #Display orders
                cursor = connection.cursor()
                cursor.execute('SELECT * FROM orders')
                # Gets all rows from the result
                rows = cursor.fetchall()
                for row in rows:
                    print(f'Order_id:{str(row[0])}, Name: {str(row[1])}, Address: {row[2]}, Phone: {row[3]}, Status:{row[4]} ')
                

            elif user_input_orders == 2: #Add an order
                input_customer_name = input ('Please enter customer name: ')
                input_customer_address = input("Enter the customer address: ")
                input_customer_phone = input("Enter phone no.: ")
                
                cursor = connection.cursor()
                sql = ("INSERT INTO orders (customer_name,customer_address,customer_phone,status) Values (%s,%s,%s,%s)")
                val = [(input_customer_name, input_customer_address, input_customer_phone,'1')]
                cursor.executemany(sql,val)
                order_id = cursor.lastrowid# return the id from the new order
                connection.commit()
                cursor.close()

                #print list of products
                cursor = connection.cursor()
                cursor.execute('SELECT * FROM products')
                rows = cursor.fetchall()
                for row in rows:
                    print(f'Product_id:{str(row[0])}, Name: {str(row[1])}, Price: {row[2]}')
                #Input for products
                input_products_order = input("Enter product ids (comma seperated): ")
                input_products = input_products_order.split (",")
                #Convert the porduct input into product list
                data = []
                for i in input_products:
                    data.append((order_id,i))

                sql = ('''INSERT INTO order_products (order_id,product_id) VALUES (%s,%s)''')
                
                cursor.executemany(sql,data)
                connection.commit()
                cursor.close()

                #print couriers
                cursor = connection.cursor()
                cursor.execute('SELECT * FROM couriers')
                rows = cursor.fetchall()
                for row in rows:
                    print(f'Courier id:{str(row[0])}, Name: {str(row[1])}, Phone: {row[2]}')
                
                input_courier_id = input("Please enter courier id: ")
                cursor = connection.cursor()

                sql = ('''INSERT INTO order_couriers (order_id,courier_id) Values (%s,%s)''')
                val = [(order_id, input_courier_id)]
                cursor.executemany(sql,val)
                connection.commit()
                cursor.close()

            elif user_input_orders == 3:#Update status of an order
                cursor = connection.cursor()
                cursor.execute('SELECT * FROM orders')
                # Gets all rows from the result
                rows = cursor.fetchall()
                for row in rows:
                    print(f'Order_id:{str(row[0])}, Name: {str(row[1])}, Address: {row[2]}, Phone: {row[3]}, Status:{row[4]} ')

                #Get inputs for order to be updated
                input_order_id = int(input ('Please choose corresponding order id: '))

                cursor = connection.cursor()
                cursor.execute('SELECT * FROM status')
                # Gets all rows from the result
                rows = cursor.fetchall()
                for row in rows:
                    print(f'Status_id:{str(row[0])}, Status: {str(row[1])}')
                
                #INPUT  for status
                input_new_status = input("Enter the status id: ")
                sql = ("UPDATE orders SET status = %s WHERE order_id = %s")
                val = [(input_new_status, input_order_id)]
                cursor.executemany(sql,val)
                connection.commit()
                cursor.close()

            elif user_input_orders == 4:#update existing order
                cursor = connection.cursor()
                cursor.execute('SELECT * FROM orders')
                # Gets all rows from the result
                rows = cursor.fetchall()
                for row in rows:
                    print(f'Order_id:{str(row[0])}, Name: {str(row[1])}, Address: {row[2]}, Phone: {row[3]}, Status:{row[4]} ')
                
                #Get inputs for order to be updated
                input_order_id = int(input ('Please choose corresponding order id: '))

                input_customer_name = input("Please enter customer name: ")
                input_customer_address = input("Please enter customer address: ")
                input_customer_phone = input("Please enter customer phone: ")

                if input_customer_name == "":
                    pass
                else:
                    sql = ("UPDATE orders SET customer_name = %s WHERE order_id = %s")
                    val = [(input_customer_name, input_order_id)]
                    cursor.executemany(sql,val)
                    connection.commit()
                
                if input_customer_phone == "":
                    pass
                else:
                    sql = ("UPDATE orders SET customer_phone = %s WHERE order_id = %s")
                    val = [(input_customer_phone, input_order_id)]
                    cursor.executemany(sql,val)
                    connection.commit()

                if input_customer_address == "":
                    pass
                else:
                    sql = ("UPDATE orders SET customer_address = %s WHERE order_id = %s")
                    val = [(input_customer_address, input_order_id)]
                    cursor.executemany(sql,val)
                    connection.commit()
                cursor.close()

                order_id = input_order_id
                cursor = connection.cursor()
                cursor.execute('SELECT * FROM products')
                # Gets all rows from the result
                rows = cursor.fetchall()
                for row in rows:
                    print(f'Product_id:{str(row[0])}, Name: {str(row[1])}, Price: {row[2]}')

                input_products_order = input("Enter product ids: ")
                input_products = input_products_order.split (",")

                data = []
                for i in input_products:
                    data.append((order_id,i))

                sql = ('''DELETE FROM order_products  WHERE order_id = %s ''')# to avoid duplication
                sql_1 = ('''INSERT INTO order_products (order_id,product_id) Values (%s,%s)''')

                cursor.execute(sql,order_id)#delete execute
                cursor.executemany(sql_1,data)#insert execute 
                connection.commit()
                    

                cursor = connection.cursor()
                cursor.execute('SELECT * FROM couriers')
                rows = cursor.fetchall()
                for row in rows:
                    print(f'Courier id:{str(row[0])}, Name: {str(row[1])}, Phone: {row[2]}')
                    
                input_courier_id = input("Please enter courier id: ")

                cursor = connection.cursor()
                sql = ('''UPDATE order_couriers  SET courier_id = %s WHERE order_id = %s ''')
                val = [(input_courier_id, order_id)]
                cursor.executemany(sql,val)#####
                connection.commit()
                cursor.close()

            elif user_input_orders == 5:#Delete an order
                cursor = connection.cursor()
                cursor.execute('SELECT * FROM orders')
                # Gets all rows from the result
                rows = cursor.fetchall()
                for row in rows:
                    print(f'Order_id:{str(row[0])}, Name: {str(row[1])}, Address: {row[2]}, Phone: {row[3]}, Status:{row[4]} ')

                input_order_id = int(input ("Please enter the id no. of order to be deleted: "))

                sql_1 = ('DELETE FROM order_couriers WHERE order_id = %s')
                sql_2 = ('DELETE FROM order_products WHERE order_id = %s')
                
                sql = ("DELETE  FROM orders WHERE order_id = %s")
                val = [(input_order_id)]
                cursor.execute(sql_2,val)
                cursor.execute(sql_1,val)
                cursor.execute(sql,val)
                connection.commit()
                cursor.close()

            else:
                print('Invalid input.')


    else:
        print('Invalid input')

connection.close()

print('Adios Amigos!!')