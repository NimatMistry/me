
# -*- coding: UTF-8 -*-
"""
I'm in UR exam.
This is the same as the weekly exercises, fill in the functions,
and test them to see if they work.
You have 2 hours.

You need to copy this file to your me/week8 folder
You need to rename it to exercise1.py
"""
import string
import time


def greet(name="Towering Timmy"):
    """Return a greeting.
    return a string of "Hello" and the name argument.
    E.g. if given as "Towering Timmy" it should return "Hello Towering Timmy"
    """
    
    return "Hello " + str(name)


def three_counter(input_list=[1, 4, 3, 5, 7, 1, 3, 2, 3, 3, 5, 3, 7]):
    """Count the number of 3s in the input_list.
    Return an integer.
    TIP: the test will use a different input_list, so don't just return 5
    """
    count = 0

    for num in input_list:
        if num == 3:
            count += 1

    return count


def fizz_buzz():
    """Do the fizzBuzz.
    This is the most famous basic programming test of all time!
       "Write a program that prints the numbers from 1 to 100. But for
        multiples of three print "Fizz" instead of the number and for
        the multiples of five print "Buzz". For numbers which are
        multiples of both three and five print "FizzBuzz"."
            from https://blog.codinghorror.com/why-cant-programmers-program/
    Return a list that has an integer if the number isn't special, and a string
    if it is. E.g. [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, ...]
    """
    fizzBuzzList = []
    # your code here

    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            fizzBuzzList.append("FizzBuzz")
        elif i % 3 == 0:
            fizzBuzzList.append("Fizz")
        elif i % 5 == 0:
            fizzBuzzList.append("Buzz")
        else:
            fizzBuzzList.append(i)

    return fizzBuzzList


def put_behind_bars(input_string="very naughty boy"):
    """Interleave the input_string with pipes.
    Given any string, interleave it with pipes (| this character)
    e.g. "very naughty boy" should return the string
    "|v|e|r|y| |n|a|u|g|h|t|y| |b|o|y|"
    TIP: strings are pretty much lists of chars. 
         If you list("string") you get ['s', 't', 'r', 'i', 'n', 'g']
    TIP: consider using the 'join' method in Python.
    TIP: make sure that you have a pipe on both ends of the string.
    """

    return "|"+"|".join(input_string)+"|"


def pet_filter(letter="a"):
    """Return a list of pets whose name contains the character 'letter'."""
    # fmt: off
    pets = [
            "dog", "goat","pig","sheep","cattle","zebu","cat","chicken",
            "guinea pig","donkey","duck","water buffalo","western honey bee",
            "dromedary camel","horse","silkmoth","pigeon","goose","yak",
            "bactrian camel","llama","alpaca","guineafowl","ferret",
            "muscovy duck","barbary dove","bali cattle","gayal","turkey",
            "goldfish","rabbit","koi","canary","society finch","fancy mouse",
            "siamese fighting fish","fancy rat and lab rat","mink","red fox",
            "hedgehog","guppy",]
    # fmt: on
    
    cont = []

    for pet in pets:
        if str(letter) in pet:
            cont.append(pet)



    return cont


def best_letter_for_pets():
    """Return the letter that is present at least once in the most pet names.
    Reusing the pet_filter, find the letter that gives the longest list of pets
    TIP: return just a letter, not the list of animals.
    """
    import string
    
    # letters = [
    #         "a","b","c","d","e","f","g","h","i","j","k","l","m",
    #         "n","o","p","q","r","s","t","u","v","w","x","y","z",]
    
    the_alphabet = string.ascii_lowercase
   
    list_length = 0

    p_letter = []

    for aplh in the_alphabet:
        pet_list = pet_filter(aplh)
        length = len(pet_list)
        print (length)
        if length >= list_length:
            list_length = length
            p_letter = str(aplh)
    
    # print(list_length)
    # print(p_letter)

    return p_letter


def make_filler_text_dictionary():
    """Make a dictionary of random words filler text.
    There is a random word generator here:
    https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=4 
    If we set minLength=18 and maxLength=18, we will get something like this:
    >>> url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=18"
    >>> r = requests.get(url)
    >>> r.text # will get you a string, something like this:
    >>> "occipitosphenoidal"
    
    Return a dictionary where the keys are numbers, and the values are lists of
    words. e.g.
    { 
        3: ['Sep', 'the', 'yob'],
        4: ['aaaa', 'bbbb', 'cccc'],
        ...
        7: ['aaaaaaa', 'bbbbbbb', 'ccccccc']
    }
    Use the API to get the 3 words.
    
    The dictionary should have the numbers between 3 and 7 inclusive.
    (i.e. 3, 4, 5, 6, 7 and 3 words for each)
    TIP: you'll need the requests library
    """

    import requests
    my_dict = {}
    url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={leng}"
    
    for i in range(3,8):
        word_list = []
        for _ in range(3):
            r = requests.get(url.format(i))
            if r.status_code is 200:
                word = r.text
                word_list.append(word)
        my_dict[i] = word_list
    return my_dict

    # # wordFreqDic.update( {'before' : 23} )

    my_list = {}

    for key in range(3,8):
        words = []
        for number in range (3):
            url = url.format(leng = key)
            r = requests.get(url)
            if r.status_code is 200:
                word = r.text
                words.append(word)
                my_list.update({key : words})
    

    print(my_list)
    return my_list


def getRandomWord(wordList):
    import random
    wordIndex = random.randInt(0, len(wordList) - 1)
    return wordList[wordIndex]

def random_filler_text(number_of_words=200):
    """Make a paragraph of random filler text.
    Using the dictionary returned by make_filler_text_dictionary, make a
    paragraph of text using randomly picked words. Each word should be a random
    length, and a random one of the 3 words.
    Make the paragraph have number_of_words words in it.
    Return it as a string
    TIP: you'll need the random library, 
        see line 77 of week4/hangman_leadboard.py for an example.
    """
    import random
    paragraph = []
    random_dict = make_filler_text_dictionary()
    for _ in range(number_of_words):
        randomInt = random.randint(3, 7)
        random_word = getRandomWord(random_dict[randomInt])
        paragraph.append(random_word)

    # turn paragraph into a string
    return ' '.join(paragraph)


def fast_filler(number_of_words=200):
    """Reimplement random_filler_text.
    This time, the first time the code runs, save the dictionary returned
    from make_filler_text_dictionary to a file.
    On the second run, if the file already exists use it instead of going to
    the internet.
    Use the filename "dict_racey.json"
    TIP: you'll need the os and json libraries
    TIP: you'll probably want to use json dumps and loads to get the dictionary
    into and out of the file. Be careful when you read it back in, it'll
    convert integer keys to strings.

    If you get this one to work, you are a Very Good Programmer™!
    """
    import os
    import json

    my_json = "dict_racey.json"
    if os.path.exists(my_json):
        # load it
        with open(my_json) as json_file:
            random_dict = json.load(json_file)
    else:
        # create it
        random_dict = make_filler_text_dictionary()  
        # save dictionary as json file
        with open('dict_racey.json', 'w') as outfile:    
            json.dumps(random_dict, outfile)

    paragraph = []
    for _ in range(number_of_words):
        randomInt = random.randint(3, 7)
        random_word = getRandomWord(random_dict[randomInt])
        paragraph.append(random_word)
    # save my file

    return ' '.join(paragraph)


if __name__ == "__main__":
    print("greet:", greet())
    print("three_counter:", three_counter())
    print("fizz_buzz:", fizz_buzz())
    print("put_behind_bars:", put_behind_bars())
    print("pet_filter:", pet_filter())
    print("best_letter_for_pets:", best_letter_for_pets())
    print("make_filler_text_dictionary:", make_filler_text_dictionary())
    print("random_filler_text:", random_filler_text())
    print("fast_filler:", fast_filler())
    for i in range(10):
        print(i, fast_filler())
    print(
        "These are mini tests, they show you some output.",
        "\nDon't forget to run the real tests.",
        "\nThey test your code against the non-default arguments",
    )
