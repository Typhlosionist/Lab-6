#Joel Liston's file

#Returns inputted string with each digit shifted up by 3
def encode(string):
    encoded_string = ""

    for digit in string:
        temp = int(digit) + 3
        if temp > 9:
            temp -= 10
        encoded_string += str(temp)

    return encoded_string

# decodes password.
def decode(string):
    decoded_string = ""
    # Loops through each digit subtracting 3 and adding 10 if the number is negative.
    for digit in string:
        temp = int(digit) - 3
        if temp < 0:
            temp += 10
        decoded_string += str(temp)

    return decoded_string


def main():
    #Variables
    user_input = -1
    password = ""
    encoded_password = ""
    decoded_password = ""

    #User Interaction
    while user_input != '1':
        print("Program Menu")
        print("---------------------")
        print("1. Exit Program")
        print("2. Encode Password")
        print("3. Decode Stored Password")
        print()

        print("Please enter selection: ", end="")
        user_input = input()

        if user_input == '2':
            print("Please enter password: ", end="")
            password = input()
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print()
        elif user_input == '3':
            decoded_password = decode(password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            print()
            

if __name__ == "__main__":
    main()