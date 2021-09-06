import numpy as np
from string import ascii_letters, digits

# Character pool to generate key from
characters = list(ascii_letters + digits)

def generate_short_url():
  return ''.join(np.random.choice(characters, 7, False))