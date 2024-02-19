import time

def main(file_path):
    product_data = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = [p.strip() for p in line.strip().split(',')]
                product = {"ID": int(parts[0]), "Name": parts[1], "Price": float(parts[2]), "Category": parts[3]}
                product_data[product["ID"]] = product
    except FileNotFoundError:
        print(f"Data file '{file_path}' not found!")
    return product_data

def write_products(products, file_path):
    try:
        with open(file_path, 'w') as file:
            for product_id, product in products.items():
                line = f"{product['ID']}, {product['Name']}, {product['Price']}, {product['Category']}\n"
                file.write(line)
        print(f"Product data stored successfully in '{file_path}'.")
    except IOError:
        print(f"Error: Unable to write to file '{file_path}'.")

def insert(products, new_product):
    products[new_product['ID']] = new_product

def update(products, product_id, updated_info):
    if product_id in products:
        products[product_id].update(updated_info)
        print(f"Product with ID {product_id} has been updated successfully!")
    else:
        print("Product with ID not found!")

def delete(products, product_id):
    if product_id in products:
        del products[product_id]
        print(f"Product with ID {product_id} deleted successfully!")
    else:
        print("Product with ID not found!")

def search(products, key, value):
    return [product for product in products.values() if str(product.get(key, '')).lower() == str(value).lower()]

def bubble_sort_with_timing(product_data):
    product_list = list(product_data.values())
    start_time = time.time()
    n = len(product_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if product_list[j]['Price'] > product_list[j+1]['Price']:
                product_list[j], product_list[j+1] = product_list[j+1], product_list[j]
    end_time = time.time()
    print(f"Sorting time: {end_time - start_time:.6f} seconds")
    return product_list

file_path = 'product_data.txt'
product_data = main(file_path)

while True:
    print("\nMenu:")
    print("1. Insert product")
    print("2. Update product")
    print("3. Delete product")
    print("4. Search products")
    print("5. Sort products by price (Ascending)")
    print("6. Measure sorting time")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        new_product = {
            'ID': int(input("Enter The Product ID: ")),
            'Name': input("Enter The Product Name: "),
            'Price': float(input("Enter The Product Price: ")),
            'Category': input("Enter The Product Category: ")
        }
        insert(product_data, new_product)
        write_products(product_data, file_path)

    elif choice == '2':
        product_id = int(input("Product ID to update: "))
        updated_info = {
            "Price": float(input("New Price: "))
        }
        update(product_data, product_id, updated_info)
        write_products(product_data, file_path)

    elif choice == '3':
        product_id = int(input("Enter product ID to remove: "))
        delete(product_data, product_id)
        write_products(product_data, file_path)

    elif choice == '4':
        search_key = input("Search by (ID, Name, Category): ")
        search_value = input("Enter the search value: ")
        if search_key.lower() == "id":
            search_value = int(search_value)
        found_products = search(product_data, search_key, search_value)
        if found_products:
            for product in found_products:
                print(f"ID: {product['ID']}, Name: {product['Name']}, Price: {product['Price']}, Category: {product['Category']}")
        else:
            print("No products found.")

    elif choice == '5':
        sorted_data = bubble_sort_with_timing(product_data)
        for product in sorted_data:
            print(f"ID: {product['ID']}, Name: {product['Name']}, Price: {product['Price']}, Category: {product['Category']}")

    elif choice == '6':
        print("Measuring sorting time...")
        _ = bubble_sort_with_timing(product_data)

    elif choice == '7':
        print("Exiting...")
        break
    else:
        print("Invalid choice, please enter a number between 1-7.")