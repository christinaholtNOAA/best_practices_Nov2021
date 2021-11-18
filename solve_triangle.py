'''
This script will help solve for an unknown side of a right triangle
using the Pythagorean Theorem (PT) or basic trig functions.


Recall that given a right triangle, the PT states that the sum of the
square of the two legs of a triangle (the short sides) is equal to the
square of its hypotenuse (the long side).

The sin, cos, and tan functions may also be used to solve for unknown
sides, and angles between them.

A user can provide 2 of the three sides when calling main, and then run
the script to determine what the unknown side is.

Requirements:

    The PT and trig funtions require all inputs to be positive
    The PT and trig function assume the hypotenuse is the longest side -- by definition.
    The code implementation requires that angles be provided in degrees.
'''

import argparse
import math
import sys

def apply_pythagorean_theorem(hypotenuse=None, leg_a=None, leg_b=None):
    ''' Solve the the pythagorean theorem given 2 of 3 user inputs.

    Pythagorean Theorem:

        hypotenuse^2 = leg_a^2 + leg_b^2

    Input:

        Ordered list of values in the following order:

        leg_a        length of one of the legs
        leg_b        length of the other leg
        hypotenuse   length of the hypotenuse

    Output:

        None
    '''


    if hypotenuse is None:
        hypotenuse = math.sqrt(pow(leg_a, 2) + pow(leg_b, 2))
        return hypotenuse

    if leg_a is None:
        leg_a = math.sqrt(pow(hypotenuse, 2) - pow(leg_b, 2))
        return leg_a

    # Solve for leg_b
    leg_b = math.sqrt(pow(hypotenuse, 2) - pow(leg_a, 2))
    return leg_b

def apply_trig_functions(unknown, opposite=None, adjacent=None,
        hypotenuse=None, theta=None):

    # pylint: disable=too-many-return-statements

    ''' Solve the basic trig function (sin, cos, tan) given triangle
    metrics.

    Recall the pneumonic: SOH, CAH, TOA

    Theta is required in radians, and is returned in radians
    '''

    if unknown == 'hypotenuse':
        if opposite:
            return opposite / math.sin(theta)
        return adjacent / math.cos(theta)

    if unknown == 'adjacent':
        if hypotenuse:
            return hypotenuse * math.cos(theta)
        return opposite / math.tan(theta)

    if unknown == 'opposite':
        if hypotenuse:
            return hypotenuse * math.sin(theta)
        return adjacent * math.tan(theta)

    # Unknown == 'theta'
    if hypotenuse:
        if opposite:
            return math.asin(opposite / hypotenuse)
        if adjacent:
            return math.acos(adjacent / hypotenuse)
    return math.atan(opposite / adjacent)

def check_sides(leg_a, leg_b, hypotenuse):

    ''' Check the values provided by the user to ensure they meet the
    contract needed by the trig functions and PT.
    '''

    if hypotenuse is None:
        return True

    if leg_a is not None:
        return leg_a < hypotenuse

    return leg_b < hypotenuse

def ensure_solvable(args):

    ''' Ensure that the necessary input is provided for a solvable
    problem. '''

    sides = ['hypotenuse', 'adjacent', 'opposite']
    num_sides = sum([1 for side in sides if args.__dict__.get(side)])

    if args.unknown == 'theta':
        return num_sides >= 2

    two_sides = num_sides >= 2
    angle_and_side = args.theta and num_sides >= 1
    return two_sides or angle_and_side

def main(clargs):

    ''' Determines which solver is required for user inputs. '''

    solvable = ensure_solvable(clargs)
    if not solvable:
        print('There is not enough information to solve this',
                'triangle.')
        sys.exit(1)

    sides_ok = check_sides(clargs.adjacent, clargs.opposite, clargs.hypotenuse)

    if not sides_ok:
        print('Sides provided by user do not meet triangle',
                'requirements!')
        sys.exit(1)

    sides = ['hypotenuse', 'adjacent', 'opposite']
    num_sides = sum([1 for side in sides if clargs.__dict__.get(side)])

    if clargs.unknown == 'theta':
        unknown_theta = apply_trig_functions(
                clargs.unknown,
                clargs.opposite,
                clargs.adjacent,
                clargs.hypotenuse,
                None) * 180 / math.pi
        print(f'The unknown theta is {unknown_theta:.2f} deg')

    if clargs.unknown in sides:
        if num_sides >= 2:
            unknown_side = apply_pythagorean_theorem(
                    hypotenuse=clargs.hypotenuse,
                    leg_a=clargs.adjacent,
                    leg_b=clargs.opposite,
                    )
        else:
            unknown_side = apply_trig_functions(
                    clargs.unknown,
                    clargs.opposite,
                    clargs.adjacent,
                    clargs.hypotenuse,
                    clargs.theta * 180 / math.pi)
            print(f'The unknown side is {unknown_side}')


def parse_args():

    ''' Set up the argparse command line arguments, and return the
    user-supplied setting.'''

    description = 'Script to solve the unknowns in a triangle.'
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('--hypotenuse',
            help="Lenght of hypotenuse",
            type=int,
            )
    parser.add_argument('--theta',
            help="Angle between two sides",
            type=int,
            )

    help_str = ("Length of one leg of the triangle. If --theta argument ",
            "is provided, this should be the length of the side ",
            "adjacent to angle identified.")
    parser.add_argument('--adjacent',
            help=''.join(help_str),
            type=int,
            )

    help_str = ("Length of one leg of the triangle. If --theta argument ",
            "is provided, this should be the length of the side ",
            "opposite the angle identified.")
    parser.add_argument('--opposite',
            help=''.join(help_str),
            type=int,
            )

    help_str = "Choice of which unknown to be determined."
    parser.add_argument('--unknown',
            choices=['opposite', 'adjacent', 'hypotenuse', 'theta'],
            help=help_str,
            )
    return parser.parse_args()


if __name__ == '__main__':

    CLARGS = parse_args()
    main(CLARGS)
