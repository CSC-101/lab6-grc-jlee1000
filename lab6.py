import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
    #purpose of the function: sorts list of book objects by titles in alphabetical order using selection sort algorithm
    #input: list of book object (list[data.Book])
    #returns: none, input list stored in place
def selection_sort_books(books: list[data.Book]) -> None:
    #for each index in list except for the last
    for idx in range(len(books) - 1):
        #find index of smallest title from current index to end of list
        mindex = index_smallest_from_titles(books, idx)
        #swap found minimum book with book at current index
        books[mindex], books[idx] = books[idx], books[mindex]

  #purpose of function: finds index of book with smallest title starting from smallest index
    #input: list of book objects and starting index
    #return: index of smallest title as an int or none if no valid index found
def index_smallest_from_titles(books: list[data.Book], start: int) -> Optional[int]:
    #check if starting index is out of bounds
    if start >= len(books) or start < 0:
        return None
        # Initialize the minimum index as the starting index
    mindex = start
    # Loop through the list starting from the next index
    for idx in range(start + 1, len(books)):
        # Compare titles to find the smallest
        if books[idx].title < books[mindex].title:
            mindex = idx  # Update minimum index if a smaller title is found

    return mindex  # Return the index of the smallest title

# Part 2
def swap_case(s: str) -> str:
    #purpose of function: swap case of each letter in input string
    #input: string with letters and non-letter characters
    #output: new string with all uppercase letters converted to lowercase and all lowercase letters converted to uppercase
    result = []
    for char in s:
            if char.isalpha():
                if char.isalpha():
                    if char.islower():
                        result.append(char.upper())
                else:
                    result.append(char.lower())
            else:
                result.append(char)
                #non-alpha characters remain unchanged
    return ''.join(result)

# Part 3
def str_translate(input_str: str, old: str, new: str) -> str:
    #purpose of function: replace all occurrences of old character with new character in input string
    #input: inputted characters to be replaced
    #return: new string with old replaced by new

    # Initialize an empty result string
    result = ''

    # Loop through each character in the input string
    for char in input_str:
        # Check if the character is the old character
        if char == old:
            # If it is, append the new character to the result
            result += new
        else:
            # Otherwise, append the original character
            result += char

    return result

# Part 4
def histogram(input_str: str) -> dict:
    #purpose of function: creates histogram mapping words to their counts in input string
    #input: string to analyze for word frequency
    #output: dictionary mapping words to frequency counts
    # Initialize an empty dictionary to hold the word counts
    word_count = {}

    # Split the input string into words
    words = input_str.split()

    # Iterate over each word in the list of words
    for word in words:
        # Normalize the word to lowercase to ensure case-insensitivity
        word = word.lower()
        # If the word is already in the dictionary, increment its count
        if word in word_count:
            word_count[word] += 1
        else:
            # Otherwise, add the word to the dictionary with a count of 1
            word_count[word] = 1

    return word_count