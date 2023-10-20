def reverse_roma(roma):
    roma_dict = {"I": 1, "V": 5, "X": 10,
                 "L": 50,  "C": 100,  "D": 500,  "M": 1000}

    sum = 0
    value = 0
    previous_value = 0

    for c in roma[::-1]:
        value = roma_dict[c]
        if value < previous_value:
            sum -= value
        else:
            sum += value
        previous_value = value

    return sum


def main():
    # roma = "VIII"
    # roma = "XXXXIV"
    # roma = "MMMMCMXCIX"
    # roma = "M"
    # roma = "MCCCLVII"
    roma = "DCLXVI"
    print(reverse_roma(roma))


if __name__ == "__main__":
    main()
