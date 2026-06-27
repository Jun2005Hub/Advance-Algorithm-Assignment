import time


class Medicine:
    def __init__(self, medicine_id, name, category, price, quantity):
        self.medicine_id = medicine_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.medicine_id:<8} {self.name:<22} {self.category:<15} RM{self.price:<8.2f} {self.quantity:<8}"


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, medicine):
        index = self.hash_function(medicine.medicine_id)
        start_index = index

        while self.table[index] is not None:
            if self.table[index].medicine_id == medicine.medicine_id:
                self.table[index] = medicine
                return "updated"

            index = (index + 1) % self.size

            if index == start_index:
                return "full"

        self.table[index] = medicine
        return "inserted"

    def search(self, medicine_id):
        index = self.hash_function(medicine_id)
        start_index = index

        while self.table[index] is not None:
            if self.table[index].medicine_id == medicine_id:
                return self.table[index]

            index = (index + 1) % self.size

            if index == start_index:
                break

        return None

    def display(self):
        print("\n" + "=" * 78)
        print("PHARMACY INVENTORY HASH TABLE")
        print("=" * 78)
        print(f"{'Bucket':<8} {'ID':<8} {'Medicine Name':<22} {'Category':<15} {'Price':<10} {'Qty':<8}")
        print("-" * 78)

        for i, medicine in enumerate(self.table):
            if medicine is None:
                print(f"{i:<8} {'Empty':<8}")
            else:
                print(f"{i:<8} {medicine}")

        print("=" * 78)


def linear_array_search(array, medicine_id):
    for medicine in array:
        if medicine.medicine_id == medicine_id:
            return medicine
    return None


def performance_test(hash_table, medicine_array):
    search_keys = [101, 105, 110, 115, 120, 999, 888, 777]

    print("\n" + "=" * 78)
    print("SEARCH PERFORMANCE COMPARISON")
    print("=" * 78)
    print("Search keys used:", search_keys)
    print("-" * 78)

    hash_start = time.perf_counter_ns()
    for key in search_keys:
        hash_table.search(key)
    hash_end = time.perf_counter_ns()
    hash_time = hash_end - hash_start

    array_start = time.perf_counter_ns()
    for key in search_keys:
        linear_array_search(medicine_array, key)
    array_end = time.perf_counter_ns()
    array_time = array_end - array_start

    print(f"{'Method':<25} {'Time Taken (ns)':<20}")
    print("-" * 78)
    print(f"{'Hash Table Search':<25} {hash_time:<20}")
    print(f"{'Array Linear Search':<25} {array_time:<20}")
    print("-" * 78)

    if hash_time < array_time:
        print("Result: Hash Table search is faster in this test.")
    else:
        print("Result: Array search is faster in this small test.")

    print("\nExplanation:")
    print("Hash Table search is usually faster because it calculates the bucket index")
    print("directly using a hash function. Array search checks records one by one.")
    print("=" * 78)


def load_sample_data(hash_table, medicine_array):
    medicines = [
        Medicine(101, "Paracetamol", "Tablet", 5.50, 100),
        Medicine(102, "Cough Syrup", "Syrup", 12.00, 50),
        Medicine(103, "Vitamin C", "Supplement", 18.90, 80),
        Medicine(104, "Antacid", "Tablet", 7.20, 60),
        Medicine(105, "Flu Medicine", "Capsule", 10.50, 70),
        Medicine(106, "Eye Drops", "Liquid", 8.90, 40),
        Medicine(107, "Pain Relief Gel", "Gel", 15.00, 30),
        Medicine(108, "Allergy Tablet", "Tablet", 9.50, 90),
        Medicine(109, "Multivitamin", "Supplement", 25.00, 45),
        Medicine(110, "Antiseptic Cream", "Cream", 13.50, 35)
    ]

    for medicine in medicines:
        hash_table.insert(medicine)
        medicine_array.append(medicine)


def print_menu():
    print("\n" + "=" * 50)
    print("LOCAL PHARMACY INVENTORY SYSTEM")
    print("=" * 50)
    print("1. Display All Medicines")
    print("2. Insert New Medicine")
    print("3. Search Medicine")
    print("4. Compare Search Performance")
    print("5. Exit")
    print("=" * 50)


def main():
    hash_table = HashTable(20)
    medicine_array = []

    load_sample_data(hash_table, medicine_array)

    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            hash_table.display()

        elif choice == "2":
            try:
                print("\n--- Insert New Medicine ---")
                medicine_id = int(input("Medicine ID: "))
                name = input("Medicine Name: ")
                category = input("Category: ")
                price = float(input("Price (RM): "))
                quantity = int(input("Quantity: "))

                medicine = Medicine(medicine_id, name, category, price, quantity)
                result = hash_table.insert(medicine)

                if result == "inserted":
                    medicine_array.append(medicine)
                    print("\nMedicine inserted successfully.")
                elif result == "updated":
                    print("\nMedicine ID already exists. Record updated successfully.")
                else:
                    print("\nHash table is full. Cannot insert new medicine.")

            except ValueError:
                print("\nInvalid input. Please enter numbers for ID, price, and quantity.")

        elif choice == "3":
            try:
                print("\n--- Search Medicine ---")
                medicine_id = int(input("Enter Medicine ID: "))
                result = hash_table.search(medicine_id)

                if result:
                    print("\nMedicine Found")
                    print("-" * 78)
                    print(f"{'ID':<8} {'Medicine Name':<22} {'Category':<15} {'Price':<10} {'Qty':<8}")
                    print("-" * 78)
                    print(result)
                    print("-" * 78)
                else:
                    print("\nMedicine not found.")

            except ValueError:
                print("\nInvalid Medicine ID. Please enter number only.")

        elif choice == "4":
            performance_test(hash_table, medicine_array)

        elif choice == "5":
            print("\nThank you for using the Pharmacy Inventory System.")
            break

        else:
            print("\nInvalid choice. Please enter 1 to 5 only.")


main()
