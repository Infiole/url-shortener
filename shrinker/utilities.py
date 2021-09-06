import numpy as np
import string

# Character pool to generate key from
characters = string.ascii_letters + string.digits

def generate_short_url():
  return ''.join(np.random.choice(characters, 7, False))