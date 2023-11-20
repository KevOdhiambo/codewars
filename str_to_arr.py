#Write a function to split a string and convert it into an array of words.
def split_string_to_array(input_string):
    # Check if the input string is empty
    if not input_string:
        return ['']
    
    # Use the split() method to split the string into words
    words_array = input_string.split()
    return words_array

# Example usage:
empty_text = 'Kevin How are you this morning'
result = split_string_to_array(empty_text)
print(result)

