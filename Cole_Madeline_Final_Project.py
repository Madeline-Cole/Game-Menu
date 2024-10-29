import random

def display_project_information():
    print("Madeline Cole \nmec399@miami.edu \nCSC 115 \nBiochemistry and Molecular Biology \nThis final project is a summary of what we have learnt this semester.")

def lottery_number_generator():
    # Generate the first five unique numbers in range 1-69
    first_five = random.sample(range(1, 70), 5)

    # Sort the first five numbers in ascending order
    first_five.sort()

    # Generate the sixth number in range 1-26
    sixth_number = random.randint(1, 26)

    # Combine the first five numbers and the sixth number into a list
    lottery_number = first_five + [sixth_number]

    # Print the lottery number without brackets
    print(*lottery_number)

def pig_latin(sentence):
    # Split the sentence into a list of words
    words = sentence.split()

    # Loop through each word and convert it to Pig Latin
    for i in range(len(words)):
        # Save the first letter of the word
        first_letter = words[i][0]

        # Remove the first letter and append it to the end of the word
        word = words[i][1:] + first_letter

        # Append "ay" to the end of the word
        word += "ay"

        # Replace the word in the list
        words[i] = word

    # Join the words back into a sentence
    pig_latin_sentence = " ".join(words)

    # Return the Pig Latin sentence
    return pig_latin_sentence

def rock_paper_scissors_game():
    options = ["rock", "paper", "scissors"]

    # Get the user's choice
    user_choice = input("Enter your choice (rock/paper/scissors): ")

    # Generate a random computer choice
    computer_choice = random.choice(options)

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("The computer wins.")

def main():
    while True:
        # Display the menu
        print("Select an option:")
        print("1. Display project information")
        print("2. Lottery Number Generator")
        print("3. Pig Latin")
        print("4. Rock, Paper, Scissors Game")

        # Get the user's choice
        choice = input("Enter your choice (1-4): ")

        # Call the appropriate function based on the user's choice
        if choice == "1":
            display_project_information()
        elif choice == "2":
            lottery_number_generator()
        elif choice == "3":
            sentence = input("Enter a sentence to convert to Pig Latin: ")
            pig_latin_sentence = pig_latin(sentence)
            print(pig_latin_sentence)
        elif choice == "4":
            rock_paper_scissors_game()
        else:
            print("Invalid choice. Please enter a number from 1-4.")

if __name__ == '__main__':
    main()
