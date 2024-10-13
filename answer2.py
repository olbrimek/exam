import random


def get_random(number: int = 3) -> list:

    # check if parameter is ok
    if not isinstance(number, int) or number <= 0 or number > 100:
        raise Exception("Invalid Data!")

    lotto_numbers = set()


    while len(lotto_numbers) < number:
        new_number = random.randint(1, 100)
        lotto_numbers.add(new_number)


    return sorted(lotto_numbers)


#print(get_random())

try:
    print(get_random(2))
except Exception as e:
    print(e)