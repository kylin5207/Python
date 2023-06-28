import numpy as np

letter_table = ord('a') + np.arange(26)
letter_table = np.char.mod('%c', letter_table)
print(letter_table)

