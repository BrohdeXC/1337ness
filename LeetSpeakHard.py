#!/bin/Python3

import sys 

def generate_leetspeak_combinations(word):
    leet_characters = {
        'A': ['a', 'A', '4', '@', '/-\\'],
        'B': ['b', 'B', '8', '13', '|3'],
        'C': ['c', 'C', '(', '<', '{'],
        'D': ['d', 'D', '|)', '|>'],
        'E': ['e', 'E', '3', '€', '[-'],
        'F': ['f', 'F', '|=', 'ph'],
        'G': ['g', 'G', '6', '9', '(_+'],
        'H': ['h', 'H', '#', '|-|', '|-|'],
        'I': ['i', 'I', '1', '!', '|'],
        'J': ['j', 'J', '_|', '_/', '¿'],
        'K': ['k', 'K', '|<', '|{'],
        'L': ['l', 'L', '|_', '|', '£'],
        'M': ['m', 'M', '|\\/|', '/\\/\\'],
        'N': ['n', 'N', '|\\|', '/\\/'],
        'O': ['o', 'O', '0', '()', '[]'],
        'P': ['p', 'P', '|°', '|>', '|*'],
        'Q': ['q', 'Q', '9', '0_', '(,)'],
        'R': ['r', 'R', '|2', '|?', '|2'],
        'S': ['s', 'S', '5', '$', '§'],
        'T': ['t', 'T', '7', '+', '†'],
        'U': ['u', 'U', '|_|', 'µ', '(_)'],
        'V': ['v', 'V', '\\/',],
        'W': ['w', 'W', '\\/\\/', '\\^/', '|/\\|'],
        'X': ['x', 'X', '><', '}{', ']['],
        'Y': ['y', 'Y', '¥', '`/'],
        'Z': ['z', 'Z', '2', '7_', '%']
    }

    def backtrack(curr_word, index):
        if index == len(word):
            combinations.append(curr_word)
            return
        for char in leet_characters.get(word[index], [word[index]]):
            backtrack(curr_word + char, index + 1)

    combinations = []
    backtrack('', 0)
    return combinations

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 LeetSpeak.py <word>")
        sys.exit(1)

    # Get the word from command-line argument
    word = sys.argv[1]


# Generate leetspeak combinations
combinations = generate_leetspeak_combinations(word.upper())

# Print the generated combinations
for combo in combinations:
    print(combo)
