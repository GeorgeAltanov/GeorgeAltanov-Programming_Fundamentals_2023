number = int(input())

for first_character in range(number):
    for second_character in range(number):
        for third_character in range(number):

            print(f"{chr(97 + first_character)}"
                  f"{chr(97 + second_character)}"
                  f"{chr(97 + third_character)}")
