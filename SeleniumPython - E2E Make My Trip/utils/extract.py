def extract_nums(string):
    number = ""
    for char in string:
        if char.isnumeric():
            num = str(char)
            number = number + num
    return int(number)


def extract_text(string):
    text = ""
    for char in string:
        if char.isalpha():
            text = text + str(char)

    return str(text)


def format_airline(string):
    text = ""
    for char in string:
        if char.isupper():
            text = text + " "
        text = text + char
    return text
