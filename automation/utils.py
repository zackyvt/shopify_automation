import random
import string

def random_phone_num_generator():
    first = str(random.randint(100, 999))
    second = str(random.randint(1, 888)).zfill(3)
    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))
    return '{}-{}-{}'.format(first, second, last)

def random_email_generator():
       return (''.join(random.choice(string.ascii_letters) for _ in range(7))) + "@" + (''.join(random.choice(string.ascii_letters) for _ in range(5))) + ".com"

def random_store_name_generator():
    return ''.join(random.choice(string.ascii_letters) for _ in range(9)).title()