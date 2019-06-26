"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random

def not_number_rejector(message):
    
    is_num = False
    num = input(message)
    while is_num == False:
        try:
            float(num)
            is_num = True
        except Exception:
            print('This is not a number, Please try again ')
            num = input(message)

    return num


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    # Start the game 
    print('Welcome to the guessing game !')
    print('Lets start by picking the range for the number')

    # Get the lower bound
    msg1 = 'Please pick the lower bound '
    lower_bound = not_number_rejector(msg1)
    
    print('Great you have enetered ' + str(lower_bound))

    # Get the upper bound
    msg2 = 'Please pick a number for the upper bound '
    upper_bound = not_number_rejector(msg2)

    # Make sure the upper bounds is a larger number than the lower bounds + 1 so there is whole number in 
    # between to guess :)
    is_smaller = False
    msg3 = 'Please select a numer higer than ' + str(int(lower_bound) + 1) + ' ' 
    
    while is_smaller == False:
      if int(upper_bound) > int(lower_bound) + 1:
        print('Cool')
        is_smaller = True
      else:
        upper_bound = not_number_rejector(msg3)
    
    print('Please guess a number between ' + str(lower_bound) + ' and ' + str(upper_bound))



    # Ask plater to guess a number 
    num_guessed = not_number_rejector(str("Please guess a number between {} and {} ".format(lower_bound, upper_bound)))


  
    # Create a loop to check if number is inside bounds 
    in_bounds = False
    
    while in_bounds == False:
      if int(num_guessed) > int(lower_bound) and int(num_guessed) < int(upper_bound):
        in_bounds = True
      elif int(num_guessed) < int(lower_bound):
        print ("Nope -_- Please stay inside the bounds")
        num_guessed = not_number_rejector(str("Please guess a number between {} and {} ".format(lower_bound, upper_bound)))
      elif int(num_guessed) > int(upper_bound):
        print ("Nope -_- Please stay inside the bounds")
        num_guessed = not_number_rejector(str("Please guess a number between {} and {} ".format(lower_bound, upper_bound)))
    


    # Pick a random number for the player to guess 
    num_selected = random.randint(int(lower_bound), int(upper_bound))


    # Creat a loop to check if the number guessed is correct 
    is_correct = False

    while is_correct == False:
      print('Your guess is {}'.format(num_guessed))
      if int(num_guessed) == int(num_selected):
        is_correct = True
      elif int(num_guessed) < int(num_selected):
        print('Sorry the number {} is too small'.format(num_guessed))
        num_guessed = not_number_rejector(str("Please guess another number between {} and {} ".format(lower_bound, upper_bound)))
      else:
        print('Sorry the number {} is too big'.format(num_guessed))
        num_guessed = not_number_rejector(str("Please guess another number between {} and {} ".format(lower_bound, upper_bound)))



    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())

