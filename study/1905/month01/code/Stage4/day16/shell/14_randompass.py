#!/usr/bin/env python3

import string
import random

key = string.ascii_letters + string.digits + '_'
password = ''
for i in range(8):
    one = random.choice(key)
    password += one

print(password)
