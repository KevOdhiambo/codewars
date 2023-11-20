#Write a function which calculates the average of the numbers in a given list.
#Note: Empty arrays should return 0.
def find_average(numbers):
    # Check if the list is empty
    if not numbers:
        return 0
    
    # Calculate the average
    average = sum(numbers) / len(numbers)
    return average
numbers_list = [3,4,100]
result = find_average(numbers_list)
print(result)