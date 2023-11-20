def string_manipulation(input_data):
    upper_case = input_data.upper()

    lower_case = input_data.lower()

    # Capitalize first letter
    capitalize_first = input_data.capitalize()

    # Count specified letters
    count_a = input_data.count('a')

    # Check if the string starts with a specific prefix
    starts_with_hello = input_data.startswith('hello')

    # Add suffix to the string
    with_suffix = input_data + ' World'

    # Print the results
    print("Original String:", input_data)
    print("Uppercase:", upper_case)
    print("Lowercase:", lower_case)
    print("Capitalize First:", capitalize_first)
    print("Count of 'a':", count_a)
    print("Starts with 'hello':", starts_with_hello)
    print("With Suffix:", with_suffix)
    print() # Extra line at the end of each function call

# Demonstrate with String
string_input = "Hello, Duck Typing!"
string_manipulation(string_input)

# Demonstrate with Int)
int_input = 12345
string_manipulation(str(int_input))

# Demonstrate with List
list_input = ['a', 'b', 'c']
string_manipulation(' '.join(list_input))
