import random

def get_random_password() -> str:
    import string
    password = random.sample(string.ascii_uppercase + string.ascii_lowercase + string.digits, 8)
    password_ = "".join(password)
    return password_

print(get_random_password())
