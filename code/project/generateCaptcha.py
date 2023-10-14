import string
from random import randint, choice, SystemRandom


def generate():
    code = ''
    for i in range(6):
        a = randint(0, 9)  # number
        b = chr(randint(65, 90))  # uppercase
        c = chr(randint(97, 122))  # lowercase

        code += str(choice([a, b, c]))

    return code


def Random():
    code = ''.join(str(SystemRandom().choice(string.ascii_letters + string.digits)) for _ in range(6))
