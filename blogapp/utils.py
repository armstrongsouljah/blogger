import random
import os
import string
from django.utils.text import slugify


def generate_unique_slug(instance, size):
    chars = string.ascii_lowercase + string.digits
    unique_code = "".join(random.choice(chars) for _ in range(size))
    unique_slug = f"{slugify(instance.name)}-{unique_code}"
    return unique_slug