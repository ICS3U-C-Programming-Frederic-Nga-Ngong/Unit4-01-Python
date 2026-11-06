#!/usr/bin/env python3
# Created By: Fred
# Date: Nov 11 2026
# Calculates the sum of numbers.


def main():

    # Get the number the user wants to know the sum to.
    usernum_str = input("Enter the last number of the list\n")

    # Verify if it is an integer
    try:
        user_num = int(usernum_str)
        sum = 0
        counter = 0
        while counter <= user_num:
            sum = sum + counter
            counter = counter + 1
            print("{} through the loop".format(counter))

        # Display the sum to the user
        print("\nThe sum of numbers from 0 to {} is {}".format(user_num, sum))

    # If the number is not an integer, tell the user to enter a valid one
    except ValueError:
        print("{} is not a valid integer. Please enter a new one.".format(usernum_str))

    # Whatever the outcome, thank to user for using the code
    print("\nThanks for using the code")


if __name__ == "__main__":

    main()
