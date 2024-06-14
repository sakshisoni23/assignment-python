'''16 Write a program in python that counts the frequency of each character in 
a string.'''

def count_character_frequency(input_string):
    frequency = {}
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
            
    return frequency

input_string = "hello world"
frequency = count_character_frequency(input_string)

for char, count in frequency.items():
    print(f"'{char}': {count}")

'''17 Write a program in python that converts a given string to title case (first 
letter of each word capitalized). '''

def convert_to_title_case(input_string):
    title_case_string = input_string.title()
    return title_case_string

input_string = "hello world"
title_case_string = convert_to_title_case(input_string)
print(title_case_string)

'''18 Write a python program that checks if two strings are anagrams of each 
other. '''
def are_anagrams(string1, string2):
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()

    return sorted(string1) == sorted(string2)

string1 = "listen"
string2 = "silent"
if are_anagrams(string1, string2):
    print("The strings are anagrams of each other.")
else:
    print("The strings are not anagrams of each other.")

'''19  Write a python program that removes all punctuation from a given string.'''
import string

def remove_punctuation(input_string):
    translator = str.maketrans("", "", string.punctuation)

    clean_string = input_string.translate(translator)
    
    return clean_string

input_string = "Hello, World! How are you today?"
clean_string = remove_punctuation(input_string)
print(clean_string)

'''20. Write a python program that takes a list of numbers and returns their sum. '''
def calculate_sum(numbers):
    return sum(numbers)

numbers = [1, 2, 3, 4, 5]
total_sum = calculate_sum(numbers)
print("Sum of the numbers:", total_sum)

'''21 Write a python program that counts the occurrences of a specific element 
in a list. '''
def count_occurrences(input_list, element):
    return input_list.count(element)

# Test the function
my_list = [1, 2, 3, 4, 2, 2, 5, 6]
element_to_count = 2
occurrences = count_occurrences(my_list, element_to_count)
print(f"The element {element_to_count} occurs {occurrences} times in the list.")

'''22. Write a python program that returns the minimum and maximum values 
in a list of numbers. '''
def find_min_max(input_list):
    if len(input_list) == 0:
        return None, None
    
    min_value = min(input_list)
    max_value = max(input_list)
    
    return min_value, max_value

# Test the function
numbers = [1, 2, 3, 4, 5]
min_value, max_value = find_min_max(numbers)
print("Minimum value:", min_value)
print("Maximum value:", max_value)

'''23. Write a program that converts temperature from Celsius to Fahrenheit 
and vice versa based on user input. '''
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Conversion")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit.")
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius.")
    else:
        print("Invalid choice. Please enter either 1 or 2.")

if __name__ == "__main__":
    main()

'''24. Write a program that acts as a simple calculator. It should take two 
numbers and an operator (+, -, *, /) as input and print the result. '''
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error!"

'''25. Write a program that copies the contents of one text file to another. '''
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                destination.write(source.read())
        print("File copied successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

def main():
    source_file = input("Enter the name of the source file: ")
    destination_file = input("Enter the name of the destination file: ")
    copy_file(source_file, destination_file)

if __name__ == "__main__":
    main()


'''26. Write a program in python that checks if a string starts with a given prefix 
or ends with a given suffix. '''
def starts_with_prefix(input_string, prefix):
    return input_string.startswith(prefix)

def ends_with_suffix(input_string, suffix):
    return input_string.endswith(suffix)

def main():
    input_string = input("Enter a string: ")
    prefix = input("Enter the prefix to check: ")
    suffix = input("Enter the suffix to check: ")

    if starts_with_prefix(input_string, prefix):
        print(f"The string '{input_string}' starts with the prefix '{prefix}'.")
    else:
        print(f"The string '{input_string}' does not start with the prefix '{prefix}'.")

    if ends_with_suffix(input_string, suffix):
        print(f"The string '{input_string}' ends with the suffix '{suffix}'.")
    else:
        print(f"The string '{input_string}' does not end with the suffix '{suffix}'.")

if __name__ == "__main__":
    main()

'''27. Write a program in python that converts a string into a list of its characters.'''
def string_to_list(input_string):
    return list(input_string)

def main():
    input_string = input("Enter a string: ")
    characters_list = string_to_list(input_string)
    print("List of characters:", characters_list)

if __name__ == "__main__":
    main()









