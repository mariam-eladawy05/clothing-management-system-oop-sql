class ClothingStore:
    def _init_(self, entity_id, name):
        self.entity_id = entity_id
        self.name = name


class Product(ClothingStore):
    def _init_(self, entity_id, name, price, category):
        super()._init_(entity_id, name)
        self.price = price
        self.category = category

    def display_details(self):
        print(f"Product ID: {self.entity_id}, Name: {self.name}, Price: ${self.price}, Category: {self.category}")


class Customer(ClothingStore):
    def _init_(self, entity_id, name, email):
        super()._init_(entity_id, name)
        self.email = email

    def display_details(self):
        print(f"Customer ID: {self.entity_id}, Name: {self.name}, Email: {self.email}")



class Payment(ClothingStore):
    def _init_(self, entity_id, name, amount, method):
        super()._init_(entity_id, name)
        self.amount = amount
        self.method = method

    def display_details(self):
        print(f"Payment ID: {self.entity_id}, Name: {self.name}, Amount: ${self.amount}, Method: {self.method}")


class Discount(ClothingStore):
    def _init_(self, entity_id, name, percentage, valid_until):
        super()._init_(entity_id, name)
        self.percentage = percentage
        self.valid_until = valid_until

    def display_details(self):
        print(f"Discount ID: {self.entity_id}, Name: {self.name}, Percentage: {self.percentage}%, Valid Until: {self.valid_until}")



class Staff(ClothingStore):
    def _init_(self, entity_id, name, position):
        super()._init_(entity_id, name)
        self.position = position

    def display_details(self):
        print(f"Staff ID: {self.entity_id}, Name: {self.name}, Position: {self.position}")



class Branch(ClothingStore):
    def _init_(self, entity_id, name, location):
        super()._init_(entity_id, name)
        self.location = location

    def display_details(self):
        print(f"Branch ID: {self.entity_id}, Name: {self.name}, Location: {self.location}")



class StoreManagementSystem:
    def _init_(self):
        self.records = {
            'Product': [],
            'Customer': [],
            'Payment': [],
            'Staff': [],
            'Branch': [],
            'Discount': []
        }

    def list_categories(self):
        print("Available categories:")
        for category in self.records:
            print(f"- {category}")

    def add_record(self, record, category):
        if category in self.records:
            self.records[category].append(record)
            print("Record added successfully.")
        else:
            print("Invalid category.")

    def display_records_by_category(self, category):
        if category in self.records:
            for record in self.records[category]:
                record.display_details()
        else:
            print("Invalid category.")

    def search_record(self):
        self.list_categories()
        category = input("Enter category: ")
        entity_id = input("Enter ID to search: ")
        if category in self.records:
            for record in self.records[category]:
                if record.entity_id == entity_id:
                    record.display_details()
                    return
        print("Record not found.")

    def update_record(self):
        self.list_categories()
        category = input("Enter category: ")
        entity_id = input("Enter ID to update: ")
        attribute = input("Enter attribute to update: ")
        value = input("Enter new value: ")
        kwargs= {attribute: value}
        if category in self.records:
            for record in self.records[category]:
                if record.entity_id == entity_id:
                    for key, value in kwargs.items():
                        if hasattr(record, key):
                            if isinstance(getattr(record, attribute), float):
                                try:
                                    value = float(value) 
                                except ValueError:
                                     print("Invalid value type.")
                                     return 

                            setattr(record, key, value)
                    print("Record updated successfully.")
                    return
        print("Record not found.")

    def delete_record(self):
        self.list_categories()
        category = input("Enter category: ")
        entity_id = input("Enter ID to delete: ")
        if category in self.records:
            for record in self.records[category]:
                if record.entity_id == entity_id:
                    self.records[category].remove(record)
                    print("Record deleted successfully.")
                    return
        print("Record not found.")

    def sort_records(self, category):
        self.list_categories()
        if category in self.records:
            if self.records[category]:
                attributes = [attr for attr in self.records[category][0]._dict.keys() if not attr.startswith('_')]
                
                print("Available attributes to sort by:")
                for attr in attributes:
                    print(f"- {attr}")
                attribute = input("Enter attribute to sort by: ")
                if attribute in attributes:            
                    order = input("Enter sorting order (asc/desc): ").lower()
                    reverse = (order == 'desc')
                    self.records[category].sort(key=lambda x: getattr(x, attribute), reverse=reverse)
                    print(f"Records in {category} sorted by {attribute} ({'descending' if reverse else 'ascending'}).")
                
                else:
                    print("Invalid attribute.")
            else:
                print("No records to sort.")
        else:
            print("Invalid category.")

system = StoreManagementSystem()
print("Welcome To M&Zs Clothing Store Maangement System!")
while True:
    print("1. Add Record")
    print("2. Display Records by Category")
    print("3. Search Record")
    print("4. Update Record")
    print("5. Delete Record")
    print("6. Sort Records")
    print("7. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        category = input("Enter category (Product/Customer/Payment/Discount/Staff/Branch): ")
        entity_id = input("Enter ID: ")
        name = input("Enter Name: ")

        if category == 'Product':
            price = float(input("Enter Price: "))
            category_type = input("Enter Category: ")
            system.add_record(Product(entity_id, name, price, category_type), category)

        elif category == 'Customer':
            email = input("Enter Email: ")
            system.add_record(Customer(entity_id, name, email), category)

        elif category == 'Payment':
            amount = float(input("Enter Amount: "))
            method = input("Enter Method: ")
            system.add_record(Payment(entity_id, name, amount, method), category)
        
        elif category == 'Discount':
                percentage = float(input("Enter Discount Percentage: "))
                valid_until = input("Enter Valid Until Date: ")
                system.add_record(Discount(entity_id, name, percentage, valid_until), category)

        elif category == 'Staff':
            position = input("Enter Position: ")
            system.add_record(Staff(entity_id, name, position), category)

        elif category == 'Branch':
            location = input("Enter Location: ")
            system.add_record(Branch(entity_id, name, location), category)


    elif choice == '2':
        category = input("Enter category to display (Product/Customer/Payment/Discount/Staff/Branch): ")
        system.display_records_by_category(category)


    elif choice == '3':
        system.search_record( )

    elif choice == '4':
        system.update_record()


    elif choice == '5':        
        system.delete_record()


    elif choice == '6':
        system.sort_records()


    elif choice == '7':
        print("Thank you for using our management system!")
        break


    else:
        print("Invalid choice!")

#Mariam Eladawy - 231000469 and Zeyna Nader - 231000000