try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    
    result_sum = a + b
    
    print(f"The result after adding {a} and {b} is: {result_sum}")
except ValueError:
    print("Please enter a valid number!")