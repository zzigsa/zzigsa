#이메일 url로전송관련된거
import string
import random

def generate_random_string(length=60):
    choice_set = string.ascii_letters + string.digits
    return ''.join(random.choices(choice_set, k=length))

