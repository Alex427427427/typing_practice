# Created by Alexander Li
# Date: 17/11/23
# Program that generates list of letters to be typed

import random
import string

# Function that generates a list of random letters
def generate_string(string_length):
    # Initialize variables
    letter_list = []
    letter = ""
    # Generate a list of random letters
    for i in range(0, string_length):
        letter = random.choice(string.ascii_letters)
        letter_list.append(letter)
    return letter_list

# if the namespace is main, run the program
if __name__ == "__main__":
    # repeatedly
    # ask the user for a number of letters to generate, exit program if 0
    while True:
        try:
            num_letters = int(input("How many letters would you like to generate? "))
            if num_letters == 0:
                break
        except ValueError:
            print("Please enter a valid number")
            continue
        # generate a list of random letters
        letter_list = generate_string(num_letters)
        # print the list of letters as a single string and ask for the user to type it
        print("The letters are: ")
        print("".join(letter_list))
        print("Type the letters above:")
        user_input = input()
        # check if the whole string was typed correctly
        if user_input == "".join(letter_list):
            print("Correct!")
        # else print the number of incorrect letters
        else:
            incorrect = abs(len(user_input) - len(letter_list))
            if len(user_input) > len(letter_list):
                for i in range(0, len(letter_list)):
                    if user_input[i] != letter_list[i]:
                        incorrect += 1
            else:
                for i in range(0, len(user_input)):
                    if user_input[i] != letter_list[i]:
                        incorrect += 1
            print("Incorrect: " + str(incorrect) + " letters typed wrongly")
        print("\n")