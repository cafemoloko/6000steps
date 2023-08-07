import os

LAST_NUMBER_FILE = 'last_number.txt'

def get_last_number():
    if os.path.exists(LAST_NUMBER_FILE):
        with open(LAST_NUMBER_FILE, 'r') as f:
            last_number = int(f.read())
        return last_number
    return 0

def update_last_number(number):
    with open(LAST_NUMBER_FILE, 'w') as f:
        f.write(str(number))
        
def increment_last_number():
    last_number = get_last_number()
    incremented_number = last_number + 1
    update_last_number(incremented_number)
    return incremented_number

def print_last_number():
    last_number_used = get_last_number()
    print(f'Last photo number: {last_number_used}')
