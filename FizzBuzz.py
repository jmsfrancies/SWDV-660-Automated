# Main Function that stores the fizz buzz test
def main():
    for i in range(1, 101):
        # If the number modulo 3 and modulo 5 equals zero, then the phrase "Fizz Buzz" is printed.
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz Buzz")
        # If the modulo 5 doesn't equal 0 and the modulo 3 does equal 0, then "Fizz" is printed
        elif i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        # If the number modulo 3 doesn't equal 0 and the modulo 5 does equal 0, then "Buzz" is printed
        elif i % 3 != 0 and i % 5 == 0:
            print("Buzz")
        # If neither modulo 3 and 5 don't equal 0, then the number is printed instead
        else:
            print(i)


main()
