#To be implemented - when we come back to framework again

import string
import random

def generate_random_emailID_and_password(domain=None, email_prefix=None):

    if not domain:
        domain = 'gmail.com'

    if not email_prefix:
        email_prefix = 'testuser'

    random_email_string_length = 10