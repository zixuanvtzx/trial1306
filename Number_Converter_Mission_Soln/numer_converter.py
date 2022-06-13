# for loop
def bin_to_den(bin_num):
    result = 0
    for i in range(len(bin_num)):
        result += int(bin_num[i]) * (2 ** (len(bin_num) - i - 1))

    return result


# while loop
def bin_to_den(bin_num):
    i = 0
    result = 0

    while i < len(bin_num):
        result += int(bin_num[i]) * (2 ** (len(bin_num) - i - 1))
        i += 1

    return result


# recursion
def bin_to_den(bin_num):
    if len(bin_num) == 0:
        return 0
    else:
        return bin_to_den(bin_num[:-1]) * 2 + int(bin_num[-1])


# print(bin_to_den("0"))  # 0
# print(bin_to_den("101"))  # 5
# print(bin_to_den("1111"))  # 15
# print(bin_to_den("11111110"))  # 254


# while loop
def den_to_bin(den_num):
    if den_num == 0:
        return "0"

    result = ""

    while den_num > 0:
        result += str(den_num % 2)
        den_num //= 2

    return result[::-1]


# recursion
def den_to_bin(den_num):
    if den_num == 0:
        return "0"
    elif den_num // 2 == 0:
        return str(den_num % 2)
    else:
        return den_to_bin(den_num // 2) + str(den_num % 2)


# print(den_to_bin(0))  # "0"
# print(den_to_bin(5))  # "101"
# print(den_to_bin(15))  # "1111"
# print(den_to_bin(254))  # "11111110"

valid_digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def value_to_symbol(val):
    return valid_digits[val]


def symbol_to_value(sym):
    return valid_digits.find(sym)


# print(value_to_symbol(7))  # "7"
# print(value_to_symbol(15))  # "F"
# print(value_to_symbol(26))  # "Q"
# print(symbol_to_value("7"))  # 7
# print(symbol_to_value("F"))  # 15
# print(symbol_to_value("Q"))  # 26


# recursion
def any_to_den(any_num, base):
    if len(any_num) == 0:
        return 0
    else:
        return any_to_den(any_num[:-1], base) * base + \
            symbol_to_value(any_num[-1])


# print(any_to_den("0", 16))  # 0
# print(any_to_den("FE", 16))  # 254
# print(any_to_den("57", 8))  # 47
# print(any_to_den("FE", 25))  # 389


# while loop
def den_to_any(den_num, base):
    if den_num == 0:
        return "0"

    result = ""

    while den_num > 0:
        result += value_to_symbol(den_num % base)
        den_num //= base

    return result[::-1]


# print(den_to_any(0, 16))  # "0"
# print(den_to_any(254, 16))  # "FE"
# print(den_to_any(47, 8))  # "57"
# print(den_to_any(389, 25))  # "FE"


def bin_to_hex(bin_num):
    result = ""

    while len(bin_num) > 0:
        group = bin_num[-4:]
        result += value_to_symbol(bin_to_den(group))
        bin_num = bin_num[:-4]

    return result[::-1]


# print(bin_to_hex("0"))  # "0"
# print(bin_to_hex("11111100"))  # "FC"
# print(bin_to_hex("111111100"))  # "1FC"
# print(bin_to_hex("1111100"))  # "7C"
# print(bin_to_hex("1111000011"))  # "3C3"


def add_front_zeros(s, total_length):
    return "0" * (total_length - len(s)) + s


# print(add_front_zeros("23", 4))


def hex_to_bin(hex_num):
    result = ""

    for i in range(len(hex_num)):
        curr_bin = den_to_bin(symbol_to_value(hex_num[i]))
        if i == 0:
            result += curr_bin
        else:
            result += add_front_zeros(curr_bin, 4)

    return result


# print(hex_to_bin("0"))  # "0"
# print(hex_to_bin("FC"))  # "11111100"
# print(hex_to_bin("1FC"))  # "111111100"
# print(hex_to_bin("7C"))  # "1111100"
# print(hex_to_bin("3C3"))  # "1111000011"

def validate_menu_opt(user_input):
    if len(user_input) == 0:  # Presence check
        print("Presence check failed. Please do not enter an empty input.")
        return False
    elif not user_input.isdigit():  # Type check
        print("Type check failed. Please enter a digit.")
        return False
    elif int(user_input) < 1 or int(user_input) > 2:  # Range check
        print("Range check failed. Please key in a value in between 1 and 2.")
        return False
    else:
        return True


# print(validate_menu_opt(""))  # Presence check
# print(validate_menu_opt("a"))  # Type check
# print(validate_menu_opt("0"))  # Range check
# print(validate_menu_opt("3"))  # Range check
# print(validate_menu_opt("1"))  # Valid


def validate_base(user_input):
    if len(user_input) == 0:  # Presence check
        print("Presence check failed. Please do not enter an empty input.")
        return False
    elif not user_input.isdigit():  # Type check
        print("Type check failed. Please enter a digit.")
        return False
    elif int(user_input) < 2 or int(user_input) > 36:  # Range check
        print("Range check failed. Base entered should be between 2 and 36.")
        return False
    else:
        return True


# print(validate_base(""))  # Presence check
# print(validate_base("a"))  # Type check
# print(validate_base("1"))  # Range check
# print(validate_base("37"))  # Range check
# print(validate_base("2"))  # Valid


def validate_num(user_input, base):
    user_input = user_input.upper()

    if len(user_input) == 0:  # Presence check
        print("Presence check failed. Please do not enter an empty input.")
        return False
    else:
        for digit in user_input:
            if digit not in valid_digits:  # Type check
                print("Type check failed. Please enter a valid digit.")
                return False

            digit_value = symbol_to_value(digit)
            if digit_value < 0 or digit_value >= base:  # Range check
                print("Range check failed. Base " + str(base) +
                      " can only accept digits between 0 and " +
                      value_to_symbol(base-1) + ".")
                return False
        return True


# print(validate_num("", 10))  # Presence check
# print(validate_num("-", 10))  # Type check
# print(validate_num("2", 2))  # Range check
# print(validate_num("A", 10))  # Range check
# print(validate_num("G", 16))  # Range check
# print(validate_num("FFG", 16))  # Range check
# print(validate_num("XYZ", 36))  # Valid


def valid_user_input(validate_func, msg, opt_arg=None):
    done = False
    while not done:
        user_input = input(msg)
        if opt_arg is None:
            done = validate_func(user_input)
        else:
            done = validate_func(user_input, opt_arg)
    return user_input


def display_menu():
    menu_opts = """
Please select the following options:
1. Number Conversion
2. Quit
    """
    print(menu_opts)


def menu():
    done = False
    while not done:
        display_menu()
        user_input = int(valid_user_input(validate_menu_opt,
                         "Please select an option 1 to 2: "))
        if user_input == 1:
            input_base = int(valid_user_input(
                validate_base, "Please select the base of input number: "))
            input_num = valid_user_input(
                validate_num, "Please enter a number of base " +
                str(input_base) + ":", input_base)
            output_base = int(valid_user_input(
                validate_base, "Please select the base of output number: "))

            output_num = den_to_any(any_to_den(
                input_num, input_base), output_base)

            print()
            print("The base for input is: " + str(input_base))
            print("The number for input is: " + input_num)
            print("The base for output is: " + str(output_base))
            print("The number for output is: " + output_num)

        elif user_input == 2:
            done = True


# menu()
