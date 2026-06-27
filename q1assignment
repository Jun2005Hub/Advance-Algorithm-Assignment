import time
import threading


# ============================================
# Factorial Function
# Time Complexity: O(n)
# ============================================

def factorial(n):

    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


# ============================================
# Function Used by Each Thread
# ============================================

def threaded_factorial(n, results):

    results[n] = factorial(n)


# ============================================
# Run Factorial Using Multithreading
# ============================================

def run_with_multithreading():

    numbers = [50, 100, 200]
    results = {}
    threads = []

    start_time = time.perf_counter_ns()

    for n in numbers:

        thread = threading.Thread(
            target=threaded_factorial,
            args=(n, results)
        )

        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.perf_counter_ns()

    total_time = end_time - start_time

    return total_time, results


# ============================================
# Run Factorial Without Multithreading
# ============================================

def run_without_multithreading():

    numbers = [50, 100, 200]
    results = {}

    start_time = time.perf_counter_ns()

    for n in numbers:
        results[n] = factorial(n)

    end_time = time.perf_counter_ns()

    total_time = end_time - start_time

    return total_time, results

# ============================================
# Display Factorial Result Preview
# ============================================

def show_factorial_preview(results):

    print("\n")
    print("=" * 100)
    print("FACTORIAL RESULT PREVIEW".center(100))
    print("=" * 100)

    print(f"{'Number':<15}{'Factorial Preview'}")
    print("-" * 100)

    for n, value in results.items():

        value_text = str(value)

        if len(value_text) > 70:
            preview = value_text[:70] + "..."
        else:
            preview = value_text

        print(f"{str(n) + '!':<15}{preview}")

    print("=" * 100)


# ============================================
# Run 10-Round Experiment
# ============================================

def run_experiment():

    threaded_times = []
    normal_times = []

    print("\n")
    print("=" * 90)
    print("QUESTION 3: FACTORIAL MULTITHREADING EXPERIMENT".center(90))
    print("=" * 90)
    print("Numbers calculated : 50!, 100!, and 200!")
    print("Testing rounds     : 10")
    print("Time unit          : Nanoseconds")
    print("=" * 90)

    # ========================================
    # Experiment 1: With Multithreading
    # ========================================

    print("\n")
    print("=" * 90)
    print("EXPERIMENT 1: WITH MULTITHREADING".center(90))
    print("=" * 90)

    print(f"{'Round':<15}{'Time Taken (ns)':<25}{'Status'}")
    print("-" * 90)

    for round_no in range(1, 11):

        time_taken, threaded_results = run_with_multithreading()
        threaded_times.append(time_taken)

        print(f"{round_no:<15}{time_taken:<25}{'Completed'}")

    threaded_average = sum(threaded_times) / len(threaded_times)

    print("-" * 90)
    print(f"{'Average':<15}{threaded_average:<25.2f}")
    print("=" * 90)

    # ========================================
    # Experiment 2: Without Multithreading
    # ========================================

    print("\n")
    print("=" * 90)
    print("EXPERIMENT 2: WITHOUT MULTITHREADING".center(90))
    print("=" * 90)

    print(f"{'Round':<15}{'Time Taken (ns)':<25}{'Status'}")
    print("-" * 90)

    for round_no in range(1, 11):

        time_taken, normal_results = run_without_multithreading()
        normal_times.append(time_taken)

        print(f"{round_no:<15}{time_taken:<25}{'Completed'}")

    normal_average = sum(normal_times) / len(normal_times)

    print("-" * 90)
    print(f"{'Average':<15}{normal_average:<25.2f}")
    print("=" * 90)

# ============================================
# Display Final Comparison
# ============================================

    print("\n")
    print("=" * 90)
    print("FINAL PERFORMANCE COMPARISON".center(90))
    print("=" * 90)

    print(f"{'Method':<35}{'Average Time (ns)':<25}{'Remarks'}")
    print("-" * 90)

    print(f"{'With Multithreading':<35}{threaded_average:<25.2f}{'3 Threads'}")
    print(f"{'Without Multithreading':<35}{normal_average:<25.2f}{'Sequential'}")

    print("-" * 90)

    if threaded_average < normal_average:
        print("\nResult:")
        print("Multithreading completed the factorial calculation faster.")
    else:
        print("\nResult:")
        print("Sequential execution completed the factorial calculation faster.")

    print("\nAnalysis")
    print("-" * 90)
    print("• The factorial function performs repeated multiplication from 1 to n.")
    print("• Therefore, its time complexity is O(n).")
    print("• Python uses the Global Interpreter Lock (GIL),")
    print("  which prevents multiple threads from executing")
    print("  CPU-intensive tasks simultaneously.")
    print("• Factorial calculation is CPU-bound, so")
    print("  multithreading may not improve performance.")
    print("• Multithreading is more suitable for I/O-bound")
    print("  applications such as downloading files,")
    print("  reading databases, or network communication.")

    print("=" * 90)

    show_factorial_preview(normal_results)


# ============================================
# Main Menu
# ============================================

def print_menu():

    print("\n")
    print("=" * 60)
    print("FACTORIAL MULTITHREADING SYSTEM".center(60))
    print("=" * 60)
    print("1. Run Performance Experiment")
    print("2. Exit")
    print("=" * 60)


# ============================================
# Main Function
# ============================================

def main():

    while True:

        print_menu()

        choice = input("Enter your choice (1-2): ")

        if choice == "1":

            run_experiment()

        elif choice == "2":

            print("\nThank you for using the program.")
            break

        else:

            print("\nInvalid choice. Please enter 1 or 2.")


# ============================================
# Run Program
# ============================================

main()
