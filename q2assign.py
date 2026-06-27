import time


class Transaction:
    def __init__(self, transaction_id, customer_name, product_name, amount, transaction_date):
        self.transaction_id = transaction_id
        self.customer_name = customer_name
        self.product_name = product_name
        self.amount = amount
        self.transaction_date = transaction_date

    def __str__(self):
        return (
            f"{self.transaction_id:<10}"
            f"{self.customer_name:<20}"
            f"{self.product_name:<25}"
            f"RM {self.amount:<12.2f}"
            f"{self.transaction_date:<15}"
        )


def display_transactions(transactions, title="CUSTOMER TRANSACTION LIST"):
    print("\n" + "=" * 100)
    print(title.center(100))
    print("=" * 100)
    print(f"{'ID':<10}{'Customer Name':<20}{'Product Name':<25}{'Amount':<15}{'Date':<15}")
    print("-" * 100)

    for transaction in transactions:
        print(transaction)

    print("=" * 100)


def merge_sort(transactions, counter=None):
    if counter is not None:
        counter["calls"] += 1

    if len(transactions) <= 1:
        return transactions

    # Divide step
    middle = len(transactions) // 2
    left_part = transactions[:middle]
    right_part = transactions[middle:]

    # Conquer step
    left_part = merge_sort(left_part, counter)
    right_part = merge_sort(right_part, counter)

    # Combine step
    return merge(left_part, right_part)


def merge(left, right):
    sorted_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i].transaction_id < right[j].transaction_id:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    while i < len(left):
        sorted_list.append(left[i])
        i += 1

    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list


def binary_search(transactions, target_id):
    low = 0
    high = len(transactions) - 1
    comparisons = 0

    start_time = time.perf_counter_ns()

    while low <= high:
        comparisons += 1
        middle = (low + high) // 2

        if transactions[middle].transaction_id == target_id:
            return transactions[middle], comparisons, time.perf_counter_ns() - start_time

        elif target_id < transactions[middle].transaction_id:
            high = middle - 1

        else:
            low = middle + 1

    return None, comparisons, time.perf_counter_ns() - start_time


def linear_search(transactions, target_id):
    comparisons = 0
    start_time = time.perf_counter_ns()

    for transaction in transactions:
        comparisons += 1

        if transaction.transaction_id == target_id:
            return transaction, comparisons, time.perf_counter_ns() - start_time

    return None, comparisons, time.perf_counter_ns() - start_time


def display_binary_result(result, comparisons, time_taken):
    print("\n" + "=" * 100)
    print("BINARY SEARCH RESULT".center(100))
    print("=" * 100)

    if result:
        print(result)
    else:
        print("Transaction not found.")

    print("-" * 100)
    print("Algorithm Used : Binary Search")
    print("Requirement    : Data must be sorted first")
    print(f"Comparisons    : {comparisons}")
    print(f"Execution Time : {time_taken} ns")
    print("Time Complexity: O(log n)")
    print("=" * 100)


def display_linear_result(result, comparisons, time_taken):
    print("\n" + "=" * 100)
    print("LINEAR SEARCH RESULT".center(100))
    print("=" * 100)

    if result:
        print(result)
    else:
        print("Transaction not found.")

    print("-" * 100)
    print("Algorithm Used : Linear Search")
    print("Requirement    : Can work with unsorted data")
    print(f"Comparisons    : {comparisons}")
    print(f"Execution Time : {time_taken} ns")
    print("Time Complexity: O(n)")
    print("=" * 100)


def performance_comparison(transactions):
    search_keys = [1001, 1005, 1010, 1015, 9999]

    # Merge Sort performance
    merge_counter = {"calls": 0}
    merge_start = time.perf_counter_ns()
    sorted_transactions = merge_sort(transactions, merge_counter)
    merge_time = time.perf_counter_ns() - merge_start

    # Binary Search performance
    binary_start = time.perf_counter_ns()
    binary_total_comparisons = 0

    for key in search_keys:
        result, comparisons, time_taken = binary_search(sorted_transactions, key)
        binary_total_comparisons += comparisons

    binary_time = time.perf_counter_ns() - binary_start

    # Linear Search performance
    linear_start = time.perf_counter_ns()
    linear_total_comparisons = 0

    for key in search_keys:
        result, comparisons, time_taken = linear_search(transactions, key)
        linear_total_comparisons += comparisons

    linear_time = time.perf_counter_ns() - linear_start

    print("\n" + "=" * 115)
    print("ALGORITHM PERFORMANCE COMPARISON".center(115))
    print("=" * 115)
    print(f"Search Keys Used: {search_keys}")
    print("-" * 115)

    print(
        f"{'Algorithm':<25}"
        f"{'Time Taken (ns)':<22}"
        f"{'Operation Count':<20}"
        f"{'Time Complexity':<20}"
        f"{'Purpose'}"
    )

    print("-" * 115)
    print(f"{'Merge Sort':<25}{merge_time:<22}{merge_counter['calls']:<20}{'O(n log n)':<20}{'Sort records'}")
    print(f"{'Binary Search':<25}{binary_time:<22}{binary_total_comparisons:<20}{'O(log n)':<20}{'Search sorted data'}")
    print(f"{'Linear Search':<25}{linear_time:<22}{linear_total_comparisons:<20}{'O(n)':<20}{'Search one by one'}")
    print("-" * 115)

    print("=" * 115)


def load_sample_transactions():
    return [
        Transaction(1008, "Ali", "Keyboard", 120.00, "2026-05-01"),
        Transaction(1003, "Bala", "Mouse", 45.50, "2026-05-02"),
        Transaction(1012, "Chong", "Monitor", 699.00, "2026-05-03"),
        Transaction(1001, "Danish", "USB Cable", 18.90, "2026-05-04"),
        Transaction(1010, "Evelyn", "Laptop Bag", 89.00, "2026-05-05"),
        Transaction(1005, "Farah", "Webcam", 150.00, "2026-05-06"),
        Transaction(1015, "Guna", "Speaker", 220.00, "2026-05-07"),
        Transaction(1002, "Hui Min", "Power Bank", 75.00, "2026-05-08"),
        Transaction(1011, "Isaac", "SSD Drive", 350.00, "2026-05-09"),
        Transaction(1007, "Jason", "Gaming Headset", 135.00, "2026-05-10"),
        Transaction(1004, "Kelly", "Printer", 499.00, "2026-05-11"),
        Transaction(1009, "Lim", "HDMI Cable", 25.00, "2026-05-12")
    ]


def load_large_transactions():
    transactions = []

    for i in range(1000):
        transactions.append(
            Transaction(
                2000 + i,
                f"Customer{i}",
                "Sample Product",
                50.00 + i,
                "2026-06-01"
            )
        )

    return transactions


def insert_transaction(transactions):
    try:
        print("\n" + "-" * 50)
        print("INSERT NEW TRANSACTION")
        print("-" * 50)

        transaction_id = int(input("Transaction ID: "))
        customer_name = input("Customer Name: ")
        product_name = input("Product Name: ")
        amount = float(input("Amount (RM): "))
        transaction_date = input("Transaction Date (YYYY-MM-DD): ")

        transactions.append(
            Transaction(transaction_id, customer_name, product_name, amount, transaction_date)
        )

        print("\nTransaction inserted successfully.")

    except ValueError:
        print("\nInvalid input. Please enter correct data type.")


def print_menu():
    print("\n" + "=" * 70)
    print("ONLINE SHOPPING TRANSACTION SYSTEM".center(70))
    print("=" * 70)
    print("1. Display All Transactions")
    print("2. Sort Transactions Using Merge Sort")
    print("3. Search Transaction Using Binary Search")
    print("4. Search Transaction Using Linear Search")
    print("5. Insert New Transaction")
    print("6. Performance Comparison")
    print("7. Load Large Dataset for Testing")
    print("8. Exit")
    print("=" * 70)


def main():
    transactions = load_sample_transactions()
    sorted_transactions = []

    while True:
        print_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            display_transactions(transactions)

        elif choice == "2":
            display_transactions(transactions, "BEFORE SORTING")
            sorted_transactions = merge_sort(transactions)
            transactions = sorted_transactions
            display_transactions(transactions, "AFTER SORTING BY TRANSACTION ID")

        elif choice == "3":
            try:
                if not sorted_transactions:
                    sorted_transactions = merge_sort(transactions)

                target = int(input("\nEnter Transaction ID: "))
                result, comparisons, time_taken = binary_search(sorted_transactions, target)
                display_binary_result(result, comparisons, time_taken)

            except ValueError:
                print("\nInvalid Transaction ID. Please enter number only.")

        elif choice == "4":
            try:
                target = int(input("\nEnter Transaction ID: "))
                result, comparisons, time_taken = linear_search(transactions, target)
                display_linear_result(result, comparisons, time_taken)

            except ValueError:
                print("\nInvalid Transaction ID. Please enter number only.")

        elif choice == "5":
            insert_transaction(transactions)
            sorted_transactions = []

        elif choice == "6":
            performance_comparison(transactions)

        elif choice == "7":
            transactions = load_large_transactions()
            sorted_transactions = []
            print("\nLarge dataset loaded successfully.")
            print("Total transaction records: 1000")
            print("Try Binary Search and Linear Search with ID 2999.")

        elif choice == "8":
            print("\nThank you for using the Transaction System.")
            break

        else:
            print("\nInvalid choice. Please enter number from 1 to 8 only.")


main()
