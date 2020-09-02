def main():
    num_to_text = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
                   "6": "six", "7": "seven", "8": "eight", "9": "nine"}
    text_to_num = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5"}

    l = input().split()
    number_of_sessions = l[2]
    number_of_stars = l[9]

    try:
        converted_number_of_sessions = num_to_text[number_of_sessions]
    except KeyError:
        print("number_of_sessions is not in [1, 2, 3, 4, 5, 6, 7, 8, 9]")
    else:
        try:
            converted_number_of_stars = text_to_num[number_of_stars]
        except KeyError:
            print("number_of_stars is not in [one, two, three, four, five]")
        else:
            print("I completed " + converted_number_of_sessions + " sessions and I rated my experience "
                  + converted_number_of_stars + " stars")


main()
