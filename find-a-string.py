# Define a function that counts the occurrences of a sub_string within a string.
def count_substring(string, sub_string):
    counts = 0
    l = len(sub_string)
    
    # Iterate through the string using a sliding window of length 'l'.
    for i in range(len(string)):
        # Check if the substring matches the current window.
        if string[i:l+i] == sub_string:
            counts += 1
        
    return counts

if __name__ == '__main__':
    # Read the main string and the sub-string from the user.
    string = input().strip()
    sub_string = input().strip()
    
    # Call the count_substring function to count occurrences.
    count = count_substring(string, sub_string)
    
    # Print the count of sub-string occurrences.
    print(count)
    
