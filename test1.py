def reverse_string(s):
    # Convert the string to a list to allow modification
    s_list = list(s)
    
    # Initialize pointers
    start = 0
    end = len(s_list) - 1
    
    # Swap characters from the start and end until pointers meet in the middle
    while start < end:
        # Swap the characters
        s_list[start], s_list[end] = s_list[end], s_list[start]
        
        # Move the pointers towards the middle
        start += 1
        end -= 1
    
    # Convert the list back to a string
    return ''.join(s_list)

# Test the function
original_string = "Hello, World!"
print("Original string:", original_string)

reversed_string = reverse_string(original_string)
print("Reversed string:", reversed_string)
