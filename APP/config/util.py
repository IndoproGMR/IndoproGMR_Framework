import random
import string
import hashlib
import uuid


def Gen_Random_string(str_size=16, allowed_chars=string.ascii_letters + string.digits):
    return "".join(random.choice(allowed_chars) for x in range(str_size))


def Gen_Random_int(int_size=16, allowed_chars=string.digits):
    return "".join(random.choice(allowed_chars) for x in range(int_size))


def Gen_Random_sha256():
    return hashlib.sha256(Gen_Random_string().encode()).hexdigest()


def Gen_Random_UUID(hex=False):
    if hex:
        return uuid.uuid4().hex
    else:
        return str(uuid.uuid4())
