sum_of_numbers = 0


while True:
    try:
        num = float(input("Enter a number: "))


        if num < 0:
            break

        sum_of_numbers += num
    except ValueError:
        print("Negative number")
print("Sum of entered numbers:", sum_of_numbers)