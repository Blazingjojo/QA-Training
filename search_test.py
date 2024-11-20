def check_number_sign(number):
    if number > 0:
        return "Positive"
    else:
        return "Negative or Zero"

# Test case 1: Test with a positive number
result_1 = check_number_sign(5)
print(f"Test Case 1 - Input: 5, Result: {result_1}")  

# Test case 2: Test with a negative number
result_2 = check_number_sign(-3)
print(f"Test Case 2 - Input: -3, Result: {result_2}") 

# Test case 3: Test with zero
result_3 = check_number_sign(0)
print(f"Test Case 3 - Input: 0, Result: {result_3}")  