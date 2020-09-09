def convert(number_of_sessions, number_of_stars):
    num_to_text = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
                   "6": "six", "7": "seven", "8": "eight", "9": "nine"}
    text_to_num = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5"}

    if number_of_sessions in num_to_text and number_of_stars in text_to_num:
        converted_number_of_sessions = num_to_text[number_of_sessions]
        converted_number_of_stars = text_to_num[number_of_stars]
        print("I completed " + converted_number_of_sessions + " sessions and I rated my experience "
              + converted_number_of_stars + " stars")
    elif number_of_sessions not in num_to_text:
        print("Invalid number of sessions")
    else:
        print(number_of_stars)
        print("Invalid number of stars")


if __name__ == "__main__":
    l = input().split()
    convert(l[2], l[9])
