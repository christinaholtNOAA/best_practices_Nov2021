'''
This script will help solve the pythagorean theorem.
'''

import math

def main(a, b, c):
    ''' Solve the the pythagorean theorem given inputs. '''

    if c is None:
        c = math.sqrt(pow(a, 2) + pow(b, 2))
        print(f'The answer is {c}')

    if a is None:
        a = math.sqrt(pow(c, 2) - pow(b, 2))
        print(f'The answer is {a}')

    if b is None:
        b = math.sqrt(pow(c, 2) - pow(a, 2))
        print(f'The answer is {b}')

if __name__ == '__main__':

    a = 3
    b = None # Expected answer is 4
    c = 5
    main(a, b, c)
