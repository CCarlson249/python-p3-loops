#!/usr/bin/env python3
def happy_new_year():
    count = 10
    while count > 0:
        print(count)
        count -= 1
    print("Happy New Year!")
    pass


def square_integers(int_list):
    # code goes here!
    result = []
    for num in int_list:
        if isinstance(num, int):  # Check if the element is an integer
            result.append(num ** 2)  # Square the integer and append it to the result list
    return result
    pass

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

    pass
