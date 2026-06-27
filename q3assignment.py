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
# Run Single Round of Specific Method
# ============================================

def run_single_round(method):
    if method == "threaded":
        return run_with_multithreading()
    else:
        return run_without_multithreading()


# ============================================
# Run 10-Round Experiment for a Method
# ============================================

def run_ten_rounds(method):
    times = []
    results = None

    method_name = "WITH MULTITHREADING" if method == "threaded" else "WITHOUT MULTITHREADING"

    print("\n")
    print("=" * 90)
    print(f"EXPERIMENT: {method_name}".center(90))
    print("=" * 90)
    print(f"{'Round':<15}{'Time Taken (ns)':<25}{'Status'}")
    print("-" * 90)

    for round_no in range(1, 11):
        time_taken, current_results = run_single_round(method)
        times.append(time_taken)
        results = current_results

        progress = str(round_no) + "/10"
        print(f"{round_no:<15}{time_taken:<25}{'Completed (' + progress + ')'}")

    average_time = sum(times) / len(times)

    print("-" * 90)
    print(f"{'Average':<15}{average_time:<25.2f}")
    print("=" * 90)

    return average_time, results


# ============================================
# Full Test (Both Methods)
# ============================================

def run_full_experiment():
    print("\n")
    print("=" * 90)
    print("FULL EXPERIMENT: BOTH METHODS".center(90))
    print("=" * 90)
    print("Numbers calculated : 50!, 100!, and 200!")
    print("Testing rounds     : 10 rounds for each method")
    print("Time unit          : Nanoseconds")
    print("=" * 90)

    threaded_avg, threaded_results = run_ten_rounds("threaded")

    normal_avg, normal_results = run_ten_rounds("sequential")

    print("\n")
    print("=" * 90)
    print("FINAL PERFORMANCE COMPARISON".center(90))
    print("=" * 90)
    print(f"{'Method':<35}{'Average Time (ns)':<25}{'Remarks'}")
    print("-" * 90)
    print(f"{'With Multithreading':<35}{threaded_avg:<25.2f}{'3 Threads'}")
    print(f"{'Without Multithreading':<35}{normal_avg:<25.2f}{'Sequential'}")
    print("-" * 90)

    if threaded_avg < normal_avg:
        print("\nResult: Multithreading completed the factorial calculation faster.")
    else:
        print("\nResult: Sequential execution completed the factorial calculation faster.")

    show_factorial_preview(normal_results)

    return threaded_avg, normal_avg


# ============================================
# Display Menu
# ============================================

def display_menu():
    print("\n")
    print("=" * 60)
    print(" FACTORIAL MULTITHREADING PERFORMANCE SYSTEM ".center(60))
    print("=" * 60)
    print("\nSelect an option:")
    print("  [1] Run with Multithreading")
    print("  [2] Run without Multithreading (Sequential)")
    print("  [3] Run BOTH methods and compare")
    print("  [4] Exit")
    print("-" * 60)


# ============================================
# Main Function with Menu
# ============================================

def main():
    while True:
        display_menu()

        try:
            choice = input("\nEnter your choice (1-4): ").strip()

            if choice == "1":
                print("\n" + "=" * 90)
                print(" RUNNING WITH MULTITHREADING ".center(90))
                print("=" * 90)
                avg_time, results = run_ten_rounds("threaded")
                print(f"\nAverage time for multithreading: {avg_time:.2f} ns")
                show_factorial_preview(results)

            elif choice == "2":
                print("\n" + "=" * 90)
                print(" RUNNING WITHOUT MULTITHREADING ".center(90))
                print("=" * 90)
                avg_time, results = run_ten_rounds("sequential")
                print(f"\nAverage time for sequential: {avg_time:.2f} ns")
                show_factorial_preview(results)

            elif choice == "3":
                run_full_experiment()

            elif choice == "4":
                print("\n" + "=" * 60)
                print(" THANK YOU FOR USING THE SYSTEM! ".center(60))
                print("=" * 60)
                break

            else:
                print("\nInvalid choice! Please enter a number between 1 and 4.")
                continue

            if choice in ["1", "2", "3"]:
                print("\n" + "-" * 60)
                cont = input("Press Enter to continue or 'q' to quit: ").strip().lower()
                if cont == 'q':
                    print("\nGoodbye!")
                    break

        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user.")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            continue


# ============================================
# Run Program
# ============================================

if __name__ == "__main__":
    main()
