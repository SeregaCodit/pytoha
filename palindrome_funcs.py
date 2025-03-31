from configparser import DuplicateSectionError
from curses.ascii import isdigit

user_input = int(input("enter a num: "))
is_palindrome = False
text = 'Not implemented!'
delimiter = 10

def get_text(num:int, bool_data:bool=True) -> str:
    if bool_data:
        return f"{num} is palindrome!"
    else:
        return f"{num} is not palindrome!"


def get_revesed_num() -> int:
    buffer_var = user_input
    reversed_num = 0
    while True:
        num = buffer_var % delimiter
        reversed_num += num
        buffer_var -= num
        buffer_var /= delimiter

        if buffer_var > delimiter:
            reversed_num *= delimiter
        else:
            reversed_num *= delimiter
            reversed_num += buffer_var
            break
    return reversed_num



if 0 < user_input < 10:
    is_palindrome = True
    text = get_text(user_input, is_palindrome)
elif user_input <= 0 or  not user_input % delimiter:
    is_palindrome = False
    text = get_text(num=user_input, bool_data=is_palindrome)
else:
    revesed_num = get_revesed_num()
    is_palindrome = revesed_num == user_input
    text = get_text(num=user_input, bool_data=is_palindrome)

print(text)