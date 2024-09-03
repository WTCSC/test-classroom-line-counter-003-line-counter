import random
import os

from line_count import line_count

def test_line_count():
  # write random text to file.txt to make sure the function is counting the lines instead of just returning a static number
  lines = random.randint(1, 300)

  # rename file.txt to file.txt.bak if it exists
  try:
    os.rename('file.txt', 'file.txt.bak')
  except FileNotFoundError:
    pass

  with open('file.txt', 'w') as file:
    for i in range(lines):
      file.write(f'line {i}\n')

  count = line_count()

  # remove file.txt
  os.remove('file.txt')

  # rename file.txt.bak back to file.txt
  try:
    os.rename('file.txt.bak', 'file.txt')
  except FileNotFoundError:
    pass

  assert count == lines