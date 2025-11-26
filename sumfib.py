def fibonacci_sum(n):
    a, b = 0, 1
    total = 0

    for _ in range(n):
        total += a
        a, b = b, a + b

    return total


if __name__ == "__main__":
    import sys
    print("=== Fibonacci Sum Calculator ===")

    try:
        if len(sys.argv) == 2:
            n = int(sys.argv[1])

        else:
            n = int(input("Enter how many Fibonacci numbers: "))

        print("=== Program Parameters ===")
        print(f"Number of terms: {n}")

        result = fibonacci_sum(n)
        print(f"\nSum of first {n} Fibonacci numbers = {result}")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")